from http.server import HTTPServer, BaseHTTPRequestHandler
import  base64
import  re
import  requests
import urllib3
urllib3.disable_warnings()

def safe_base64_decode(s): # 解码
    try:
        if len(s) % 4 != 0:
            s = s + '=' * (4 - len(s) % 4)
        base64_str = base64.urlsafe_b64decode(s)
        return bytes.decode(base64_str)
    except Exception as e:
        print('解码错误')###

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
            print('注意检查网络，下载文件出错，对应的url地址为：'+url)

def getnodeR(s):             #获取节点信息

    config = {
    "remark": "",
    "server": "0.0.0.0",
    "server_ipv6": "::",
    "server_port": 8388,
    "password": "m",
    "method": "aes-128-ctr",
    "protocol": "auth_aes128_md5",
    "protocol_param": "",
    "obfs": "tls1.2_ticket_auth_compatible",
    "obfs_param": ""
    }

    #s = safe_base64_decode(ssr)
    spilted = re.split(':',s)  #将多个参数分离开来
    pass_param = spilted[5]
    pass_param_spilted = re.split('\/\?',pass_param)
    passwd = safe_base64_decode(pass_param_spilted[0]) #解码得到password
    try:
        obfs_param = re.search(r'obfsparam=([^&]+)',pass_param_spilted[1]).group(1)
    except:
        obfs_param=""
    try:
        protocol_param = re.search(r'protoparam=([^&]+)', pass_param_spilted[1]).group(1)
        protocol_param = safe_base64_decode(protocol_param)
    except:
        protocol_param = ''
    try:
        remarks = re.search(r'remarks=([^&]+)', pass_param_spilted[1]).group(1)
        remarks = safe_base64_decode(remarks)
    except:
        remarks = '' 

    config['remark'] = remarks
    config['server'] = spilted[0]
    config['server_port'] = int(spilted[1])
    config['password'] = passwd
    config['method'] = spilted[3]
    config['protocol'] = spilted[2]
    config['obfs'] = spilted[4]
    config['protocol_param'] = protocol_param
    config['obfs_param'] = obfs_param

    return config

def getrules():             # 自定义规则
    
    finalrules=[]
    rules = Retry_request('https://raw.githubusercontent.com/ConnersHua/Profiles/master/Clash/Pro.yaml')        #请求规则_神机规则
    p_rule= Retry_request('https://raw.githubusercontent.com/lzdnico/ToClash/master/General.yml')               #基础规则_默认不配置DNS
    #p_rule=rules.split('Proxy:')[0]                                                                            #基础规则_默认配置DNS,与上面二选一
    l_rule =  rules.split('Rule:\n')[1]
    Peoxies = 'Proxy:\n'
    finalrules.append(p_rule)
    finalrules.append(Peoxies)
    finalrules.append(l_rule)
    return finalrules

def writeRules(sublink):    #返回策略组及规则
    try:
        other=[]
        name =''        
        Peoxies = ''
        rules = getrules
        data = Retry_request(sublink)    #请求订阅        
        ssrdata=safe_base64_decode(data).strip().split('\n')  
        #ssrdata = data.strip().replace('==','').split('\n')   
         
        for i in range(len(ssrdata)):                                                   #节点组            
            ssrlink = safe_base64_decode(ssrdata[i].replace('ssr://','').replace('\r',''))
            nodeR = getnodeR(ssrlink)
            remark = nodeR['remark']
            #简单粗暴的解决一些机场节点名字重复的问题
            if remark in name:          
                continue
            name += remark               #占用空间大，不会出错
            #name = remark               #占用空间小一点，可能会出错
            #简单粗暴的解决一些机场节点名字重复的问题结束
            print(remark)
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
            Json={ 'name': remark, 'type': 'ssr', 'server': nodeR['server'], 'port': nodeR['server_port'], 'password':nodeR['password'] , \
                'cipher': nodeR['method'], 'protocol': nodeR['protocol'], 'protocolparam': nodeR['protocol_param'], 'obfs': nodeR['obfs'], 'obfsparam': nodeR['obfs_param'] }
            #print(Json)
            Peoxies +='- '+str(Json)+'\n'
            other.append(remark)
        
        ProxyGroup='\n\nProxy Group:\n\n'\
                '- { name: "😀故障切换", type: "fallback", "proxies": ' + str(other) + ', url: "http://www.gstatic.com/generate_204", interval: 300'+ '}\n\n\n'\
                '- { name: "🚀手动选择", type: "select", "proxies": ' + str(other) + '}\n\n\n'\
                '- { name: "PROXY", type: select, proxies: [ "😀故障切换","🚀手动选择","DIRECT"] }\n'\
                '- { name: "GlobalMedia", type: select, proxies: ["PROXY","🚀手动选择"] }\n'\
                '- { name: "DomesticMedia", type: select, proxies: ["DIRECT","PROXY","🚀手动选择"] }\n'\
                '- { name: "Hijacking", type: select, proxies: ["REJECT", "DIRECT"] }\n'\
                '- { name: "Apple", type: select, proxies: ["DIRECT", "PROXY"] }\n'\
                '- { name: "Final", type: select, proxies: ["PROXY", "DIRECT"] }\n\n\n'\
                'Rule:\n'
        rules = getrules()
        return rules[0]+rules[1]+Peoxies+ProxyGroup+rules[2]       #回传配
    except Exception as e:
        print('返回规则错误:',e)

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        path=self.path
        if '?' in path:  #分割请求获取订阅链接
            ssrlink=path.split('/?')[1]
            print(ssrlink)
            data = writeRules(ssrlink)
            self.send_response(200)
            self.send_header("Content-type","text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(str.encode(data))

if __name__ == '__main__':
    host = ('127.0.0.1', 8964) # 监听端口
    print('请在CFW中点击更新按钮')
    server = HTTPServer(host, Resquest)
    server.serve_forever()
