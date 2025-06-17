from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Get bot token from environment variable (Render will inject this)
TOKEN = os.getenv("BOT_TOKEN")

# Create bot instance
bot = Bot(token=TOKEN)
app = Flask(__name__)

# --- TELEGRAM BOT COMMAND HANDLERS ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I’m alive and working!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛠️ I'm a simple bot. Use /start to check if I'm working.")

# --- Set up application with handlers ---
application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))

# --- FLASK ROUTE TO HANDLE WEBHOOK ---
@app.route("/", methods=["GET"])
def home():
    return "🚀 Bot is live!"

@app.route(f"/webhook/{TOKEN}", methods=["POST"])
async def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        await application.process_update(update)
    return "✅ OK", 200

# --- MAIN RUN (local development only) ---
if __name__ == "__main__":
    print("🔧 Running locally...")
    app.run(debug=True)
