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
    print('rekply_token = ' + reply_token)
    print(req)

    reply(intent,text,reply_token,id,disname,req)
    #line_bot_api.push_message(id, TextSendMessage(text='Hello World!'))
    return 'OK'


def reply(intent,text,reply_token,id,disname,req):
    if intent == 'intent-test':
        text_message = TextSendMessage(text='คุณเริ่มอีกอาการปวดคอแล้วนะ ลองปรับเปลี่ยนท่านั่งในการทำงานไหม')
        line_bot_api.reply_message(reply_token,text_message)
    if intent == 'intent-fastdoc':
        text_message = TextSendMessage(text='สวัสดีครับ คุณ '+ disname+"\n" + 'เรา FastDoc Virtual Assitant ทางด้าน Office syndrome')
        text_message2 = TextSendMessage(
            text='คุณ '+ disname+"\n" + 'เป็นสมาชิกใน Pulse Application เรามั้ยเอ่ย? \n ถ้าใช่กรุณาใส่ email ที่ใช้สมัคร pulse')

        line_bot_api.reply_message(reply_token, [text_message, text_message2])


    # if intent == 'intent-interest':
    #     text_message = TextSendMessage(text='เพลงไหนเหมาะกับคุณมากที่สุดในวันนี้\nยิ่งใกล้ยิ่งเจ็บ - อินคา\nWith or without you - U2\nทิ้งไว้ในใจ - Big Ass\n100 เหตุผล - Ster')
    #     video_message = VideoSendMessage(
    #         original_content_url='https://example.com/original.mp4',
    #         preview_image_url='https://example.com/preview.jpg'
    #     )
    #     line_bot_api.reply_message(reply_token,[text_message,video_message])


    if intent == 'intent-symptom':
        # weight = int(req["queryResult"]['outputContexts'][0]['parameters']['weight']['amount'])#[0]['parameters'])
        # day = int(req["queryResult"]['outputContexts'][0]['parameters']['day']['amount'])
        # age = int(req["queryResult"]['outputContexts'][0]['parameters']['age'])
        # hour = int(req["queryResult"]['outputContexts'][0]['parameters']['hour']['amount'])
        # length = int(req["queryResult"]['outputContexts'][0]['parameters']['length.original'][:3])
        # bmi = weight/(length*length)
        # test_ = np.array([age,length,weight,bmi,hour,day])
        # print(test_)
        # print(age)
        text_message = TextSendMessage(text='งั้นลองมาทดสอบความตึงที่กล้ามเนื้อคอกันดีกว่า คุณ ' + disname+' ช่วยส่งวีดิโอที่หันหน้าจากซ้ายไปขวากลับมาได้ไหม')
        # video_message = VideoSendMessage(
        #     original_content_url='https://example.com/original.mp4',
        #     preview_image_url='https://example.com/preview.jpg'
        # )
        line_bot_api.reply_message(reply_token,text_message)

    # if intent == 'intent-mood':
    #
    #     mood=music.iloc[0][1]
    #     print(mood)
    #     text_message = TextSendMessage(text='วันนี้คุณดูเศร้าๆนะ ไม่เป็นไรนะ FastDoc เป็นกำลังใจให้คุณ')
    #     text_message2 = TextSendMessage(
    #         text='เย้! ถึงเวลาเลิกงานแล้วนะคุณ ' + disname+'\n วันนี้คุณจ้องคอมนานเท่าไหร่นะ?')

    # line_bot_api.reply_message(reply_token,[text_message,text_message2])

    if intent == 'intent-hour':
        text_message = TextSendMessage(text='วันนี้คุณดูเศร้าๆนะ ไม่เป็นไรนะ FastDoc เป็นกำลังใจให้คุณ')
        text_message2 = TextSendMessage(
            text='เย้! ถึงเวลาเลิกงานแล้วนะคุณ ' + disname+'\n วันนี้คุณจ้องคอมนานเท่าไหร่นะ?')

        line_bot_api.reply_message(reply_token,[text_message,text_message2])

    if intent == 'intent-yes-pulse':

        mood=music.iloc[0][1]
        print(mood)
        text_message = TextSendMessage(text='pulse account ของคุณคือ'+ disname+"1234" )
        text_message2 = TextSendMessage(
            text='สวัสดี '+ disname+"\n" + 'เรามาเช็ค mood ก่อนเริ่มงานกันดีไหม \nคุณ '+ disname+"\n" + 'คิดว่าเพลงไหนที่ตรงกับอารมณ์ของคุณวันนี้')
        text_message3 = TextSendMessage(
            text='ยิ่งใกล้ยิ่งเจ็บ - อินคา\nWith or without you - U2\nทิ้งไว้ในใจ - Big Ass\n100 เหตุผล - Ster')

        line_bot_api.reply_message(reply_token,[text_message,text_message2,text_message3])


if __name__ == '__main__':
    app.run(debug=True, port= 2000)
