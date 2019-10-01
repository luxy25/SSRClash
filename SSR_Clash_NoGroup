#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import base64
import codecs
import os
import  re
import urllib3
urllib3.disable_warnings()

def safe_base64_decode(s): # 解码
    try:
        if len(s) % 4 != 0:
            s = s + '=' * (4 - len(s) % 4)
        base64_str = base64.urlsafe_b64decode(s)
        return bytes.decode(base64_str)
    except Exception as e:
        print('解码错误:', e)

def Retry_request(url): #超时重传
    flag=True
    while flag:
        try:
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
            res = requests.get(url, headers=header, timeout=5, verify=False) # verify =false 防止请求时因为代理导致证书不安全
            if res.headers['Connection']!='close':
                flag=False
                return res.text
        except Exception as e:
            print('注意检查网络，下载文件出错，对应的url地址为：'+url,e)


def writeRules(sublink): #写回配置
    try:
        other=[]
        data = Retry_request(sublink)    #请求订阅
        ssrdata=safe_base64_decode(data).strip().split('\n')
        rules = Retry_request('https://raw.githubusercontent.com/ConnersHua/Profiles/master/Clash/Pro.yaml')        #请求规则_神机规则
        p_rule= Retry_request('https://raw.githubusercontent.com/lzdnico/ToClash/master/General.yml')               #基础规则_默认不配置DNS
        #p_rule=rules.split('Proxy:')[0]                                                                            #基础规则_默认配置DNS,与上面二选一
        l_rule =  rules.split('Rule:\n')[1]
        Peoxies = 'Proxy:\n'
        

        name =''
        for i in range(len(ssrdata)):                                                   #节点组
            
            ssrlink=safe_base64_decode(ssrdata[i].replace('ssr://', ''))
            config=re.split(':|&|=|/\?',ssrlink)
            remark1 =safe_base64_decode(config[11])


            # 匹配不同订阅格式
            if i < len(ssrdata)-1:
                ssrlink2=safe_base64_decode(ssrdata[i+1].replace('ssr://', ''))
                config2=re.split(':|&|=|/\?',ssrlink2)
                remark2 =safe_base64_decode(config2[11])

            if remark1 == remark2:
                remark =  safe_base64_decode(config[-1])
            else :
                remark = remark1
            remark2 = remark1
            # 匹配不同订阅格式结束

            #简单粗暴的解决一些机场节点名字重复的问题
            if remark in name:          
                continue
            name += remark               #占用空间大，不会出错
            #name = remark               #占用空间小一点，可能会出错
            #简单粗暴的解决一些机场节点名字重复的问题结束
            
            #接下来是给节点加图标的，需要深度自定义，可以全部删除
            if "30倍" in remark:
                continue
            if "香港" in remark:
                remark = '🇭🇰' + remark
            if "美国"  in remark or "狮城" in remark :
                remark = '🇺🇸' + remark
            if "深港" in remark  or "沪港" in remark  or "京港" in remark or "杭港" in remark:
                remark = '🇨🇳 👉👉 🇭🇰' + remark
            if "深美" in remark  or "沪美" in remark  or "京美" in remark or "杭美" in remark:
                remark = '🇨🇳 👉👉 🇺🇸' + remark
            if "深日" in remark  or "沪日" in remark  or "京日" in remark or "杭日" in remark:
                remark = '🇨🇳 👉👉 🇯🇵' + remark
            if "深台" in remark  or "沪台" in remark  or "京台" in remark or "杭台" in remark:
                remark = '🇨🇳 👉👉 🇨🇳' + remark
            #加图标到此结束

            name += remark
            print(remark)
            pwd = safe_base64_decode(config[5])
            obfsparam=safe_base64_decode(config[7])
            protoparam =safe_base64_decode(config[9])          
            Json={ 'name': remark, 'type': 'ssr', 'server': config[0], 'port': config[1], 'password':pwd , 'cipher': config[3], 'protocol': config[2], 'protocolparam': protoparam, 'obfs': config[4], 'obfsparam': obfsparam }
            #print(Json)
            Peoxies +='- '+str(Json)+'\n'
            other.append(remark)


             #策略组
        ProxyGroup='\n\nProxy Group:\n\n'\
                '- { name: "😀故障切换", type: "fallback", "proxies": ' + str(other) + ', url: "http://www.gstatic.com/generate_204", interval: 300'+ '}\n\n\n'\
                '- { name: "🚀手动选择", type: "select", "proxies": ' + str(other) + '}\n\n\n'\
                '- { name: "PROXY", type: select, proxies: [ "😀故障切换","🚀手动选择","DIRECT"] }\n'\
                '- { name: "ForeignMedia", type: select, proxies: ["PROXY","🚀手动选择"] }\n'\
                '- { name: "DomesticMedia", type: select, proxies: ["DIRECT","PROXY","🚀手动选择"] }\n'\
                '- { name: "Hijacking", type: select, proxies: ["REJECT", "DIRECT"] }\n'\
                '- { name: "Apple", type: select, proxies: ["DIRECT", "PROXY"] }\n'\
                '- { name: "Final", type: select, proxies: ["PROXY", "DIRECT"] }\n\n\n'\
                'Rule:\n'
        return p_rule+Peoxies+ProxyGroup+l_rule       #回传配置
    except Exception as e:
            print('返回规则错误:',e)


def getClash(nodes):  #写文件
    
    try:


        with codecs.open('./config.yaml', "w",encoding = 'utf-8') as f:
            f.writelines(nodes)

    
    except Exception as e:
        print('main Error:', e)

if __name__ == "__main__":
    try:
        url = ""         
        data = writeRules(url)
        getClash(data)
        input('任意键退出')
    except Exception as e:
        print('main Error:', e)
