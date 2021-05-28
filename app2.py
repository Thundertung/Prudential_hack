from flask import *
from linebot import *
from linebot.models import *
app = Flask(__name__)
line_bot_api = LineBotApi('WpiaMY5dUfFtMo17+ZPatVM4mnmkiw3V1Q2r8fjCz5gyWy/kcx4gNRANlPDSBczk1D3cNLf15UxPohFaA8HhnwovC147Rk8q5ty2uYQnt9CGD87d4rTqqNLwT+JxAHlosuWCrg0oMIGtQ2iw7pzwLAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('66ffde9e2a3ad6a65656b55abd80b702')



@app.route('/index',methods=['POST'])
def hello():
    body = request.get_data(as_text=False)
    print(body)
    # message_content = line_bot_api.get_message_content(message_id)
    # with open(file_path, 'wb') as fd:
    #     for chunk in message_content.iter_content():
    #         fd.write(chunk)
    message_content = line_bot_api.get_message_content()

    req = request.get_json(silent=True, force=True)
    intent = req["queryResult"]["intent"]["displayName"]
    text = req['originalDetectIntentRequest']['payload']['data']['message']['text']
    reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
    id = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
    disname = line_bot_api.get_profile(id).display_name

    print('id = ' + id)
    print('name = ' + disname)
    print('text = ' + text)
    print('intent = ' + intent)
    print('reply_token = ' + reply_token)
    print(req)
    #print(message_content)
    reply(intent,text,reply_token,id,disname)

    return 'OK'

def reply(intent,text,reply_token,id,disname):
    if intent == 'intent-test':
        text_message = TextSendMessage(text='ทดสอบสำเร็จ')
        video_message = VideoSendMessage(
            original_content_url='https://example.com/original.mp4',
            preview_image_url='https://example.com/preview.jpg'
        )
        line_bot_api.reply_message(reply_token,[text_message,video_message])
        #line_bot_api.reply_message(reply_token, )


# @app.route("/index", methods=['POST'])
# def callback():
#     body = request.get_data(as_text=True)
#     # print(body)
#     req = request.get_json(silent=True, force=True)
#     intent = req["queryResult"]["intent"]["displayName"]
#     text = req['originalDetectIntentRequest']['payload']['data']['message']['text']
#     reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
#     id = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
#     disname = line_bot_api.get_profile(id).display_name
#
#     print('id = ' + id)
#     print('name = ' + disname)
#     print('text = ' + text)
#     print('intent = ' + intent)
#     print('reply_token = ' + reply_token)
#
#     reply(intent,text,reply_token,id,disname)
#
#     return 'OK'
#
#
# def reply(intent,text,reply_token,id,disname):
#     if intent == 'intent-test':
#         text_message = TextSendMessage(text='ทดสอบสำเร็จ')
#         line_bot_api.reply_message(reply_token,text_message)

if __name__ == '__main__':
    app.run(debug=True, port= 2221)