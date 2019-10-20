# coding=utf-8
import sys
from flask import Flask
import flask_restful
import  base64
import  re
import  requests
import urllib3
import json
import time
urllib3.disable_warnings()

def Retry_request(url): #远程下载
    i = 0
    for i in range(3):
        try:
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
            res = requests.get(url, headers=header, timeout=5, verify=False) # verify =false 防止请求时因为代理导致证书不安全
            if res.headers['Connection']!='close':
                flag=False
                return res.text
        except Exception as e:
            i = i +1
            print('重新下载：'+url)

def getrules(link,tag):             # 自定义规则
    
    try:
        rule = Retry_request('https://raw.githubusercontent.com/lzdnico/SSRClash/master/qxconfig')        #请求规则_神机规则
        rules = str(rule).split('下方粘贴你的订阅链接')
        rules[0] += '\n' + link + ', tag=' +  tag + ', enabled=true\n'
        return rules[0] + rules[1]
    except Exception as e:
        print(e)

app = Flask(__name__)

@app.route('/')
def my():
    return 'STC API 使用教程：<br/><br/>'

@app.route('/<name>',methods=['GET'])
def get(name):
    name = name.replace('!','/')    
    link = name.split('@')[0]
    tag =  name.split('@')[1]
    return getrules(link,tag)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=2333)
