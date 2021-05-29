from flask import *
from linebot import *
from linebot.models import *
import numpy as np
import pandas as pd
app = Flask(__name__)
line_bot_api = LineBotApi('WpiaMY5dUfFtMo17+ZPatVM4mnmkiw3V1Q2r8fjCz5gyWy/kcx4gNRANlPDSBczk1D3cNLf15UxPohFaA8HhnwovC147Rk8q5ty2uYQnt9CGD87d4rTqqNLwT+JxAHlosuWCrg0oMIGtQ2iw7pzwLAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('66ffde9e2a3ad6a65656b55abd80b702')
music = pd.read_csv('prudential_mood.csv')


@app.route('/index',methods=['POST'])
def hello():
    body = request.get_data(as_text=False)
    print(body)

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

    reply(intent,text,reply_token,id,disname,req)

    return 'OK'


def reply(intent,text,reply_token,id,disname,req):
    if intent == 'intent-test':
        text_message = TextSendMessage(text='ผลการตรวจนะค่ะ\n'
                                            'ไปหาหมอหน่อยนะค่ะ คุณมีโอกาสเป็นกล้ามเนื้ออักเสบ')
        video_message = VideoSendMessage(
            original_content_url='https://example.com/original.mp4',
            preview_image_url='https://example.com/preview.jpg'
        )
        line_bot_api.reply_message(reply_token,[text_message,video_message])


    if intent == 'intent-symptom':
        weight = int(req["queryResult"]['outputContexts'][0]['parameters']['weight']['amount'])#[0]['parameters'])
        day = int(req["queryResult"]['outputContexts'][0]['parameters']['day']['amount'])
        age = int(req["queryResult"]['outputContexts'][0]['parameters']['age'])
        hour = int(req["queryResult"]['outputContexts'][0]['parameters']['hour']['amount'])
        length = int(req["queryResult"]['outputContexts'][0]['parameters']['length.original'][:3])
        bmi = weight/(length*length)
        test_ = np.array([age,length,weight,bmi,hour,day])
        print(test_)
        print(age)
        text_message = TextSendMessage(text='เพื่อความแม่นยำที่มากขึ้นเราขอรบกวน user ช่วยถ่ายวีดีโอ พร้อมบอกจุดที่มีอาการปวดด้วยค่ะ')
        # video_message = VideoSendMessage(
        #     original_content_url='https://example.com/original.mp4',
        #     preview_image_url='https://example.com/preview.jpg'
        # )
        line_bot_api.reply_message(reply_token,text_message)

    if intent == 'intent-mood':

        mood=music.iloc[0][1]
        print(mood)
        text_message = TextSendMessage(text='วันนี้มาแนวเศร้าๆ\nเดี่ยวเราจะช่วยเรื่อง Office symdrome ให้นะคะ\n'
                                            'กรุณาบอกข้อมูล อายุ ส่วนสูง เพศ ชม การทำงาน และ จำนวนวันทำงานด้วยค่ะ')

        line_bot_api.reply_message(reply_token,text_message)





if __name__ == '__main__':
    app.run(debug=True, port= 2000)
