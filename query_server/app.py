# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from config import Token
import time
from flask import  make_response
import hashlib
import xml.etree.ElementTree as ET

app = Flask(__name__)

f = open("result.txt")
lines = f.readlines()
print(len(lines))
day_pos_dic = {}
for line in lines:
    day_pos_dic[line.split(" ")[0]] = line.split(" ")[1]
    
print("Init Done!")

def get_response(birthday):
    if birthday not in day_pos_dic.keys():
        result = "抱歉，请输入合法的八位数生日（如20200101）"
    else:
        result = '您好！您的生日\"' + birthday + '\"出现在π的第' + day_pos_dic[birthday].replace("\n", '') + '位'
    return result

# ...
def reply_text(to_user, from_user, content):
    reply = """
    <xml><ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    <FuncFlag>0</FuncFlag></xml>
    """
    response = make_response(reply % (to_user, from_user, str(int(time.time())), content))
    response.content_type = 'application/xml'
    return response


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/authorize', methods=['GET'])
def authorize():
    signature = request.args.get('signature')
    echostr = request.args.get('echostr')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    msg = [Token, timestamp, nonce]
    msg.sort()
    hashCode = hashlib.sha1(''.join(msg).encode()).hexdigest()
    print("get sig " + signature)
    print("get echostr " + echostr)
    print("get timestamp " + timestamp)
    print("get nonce " + nonce)
    print("hash " + hashCode)
    print(hashCode == signature)
    if hashCode == signature:
        return echostr
    else:
        return "success"
    return 'error'

@app.route('/authorize', methods=['POST'])
def returnpos():
    xml = ET.fromstring(request.data)
    toUser = xml.find('ToUserName').text
    fromUser = xml.find('FromUserName').text
    msgType = xml.find("MsgType").text

    if msgType == 'text':
        content = xml.find('Content').text
        return reply_text(
            fromUser, toUser, get_response(content))
    else:
        return reply_text(fromUser, toUser, "嗯？我听不太懂")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, threaded=True)