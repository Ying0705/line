from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('KIwbm4b9dnUTcOi3y29blnghK7fF3+GFV5xoSQ4ItXR/fI0/sfnGJUrLWYfT9M6J8Nzpn8YmR1fX7mrmcfJlfl80XzO7O+RUeg7Cwxb3ner18vvFkoYZKya4ekOy3JKKHWot/zPHnx4KAWFJC2wJ5wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2f118a3c37b90dd452b156c46a1e7539')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "What do you ask?"

    if msg == "hi" :
        r == "hi"  
    elif msg == "Do you eat at all?" :
        r == "not yet"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r)


if __name__ == "__main__":
    app.run()