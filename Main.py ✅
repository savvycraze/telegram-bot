from flask import Flask, request
import telegram

BOT_TOKEN = "7953788081:AAHHFJ64BzmMY-pnw2eiSh4BELX-qhIs13g"
BOT_USERNAME = "savvycraze_bot"

bot = telegram.Bot(token=BOT_TOKEN)
app = Flask(__name__)

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message = update.message.text

    if message == "/start":
        bot.send_message(chat_id=chat_id, text="Hello! I'm alive and running on Render!")

    return "OK"

@app.route("/")
def index():
    return "Bot is running."

if __name__ == "__main__":
    app.run(debug=True)