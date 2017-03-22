'''
Created on 2017年3月19日

@author: colclo
'''
from urllib import request
import json

access_token = ''

#获取access_token
user = dict(username='YOUR_USERNAME',password='YOUR_PASSWORD')
login_data = json.dumps(user)
req = request.Request('https://api.zoomeye.org/user/login')
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    access_token=json.loads(f.read().decode('utf-8'))['access_token']


#读取需要查询的文件(文件中ip得是一行一条的形式)
with open(r'C:\Users\Administrator\Desktop\source.txt', 'r',encoding='utf-8',errors='ignore') as r:
    with open(r'C:\Users\Administrator\Desktop\zzz.txt', 'w', encoding='utf-8') as w:
        print('开始查询：')
        line = r.readline()
        while line:
            print(line.strip()+'......')
            #发送get请求查询该ip
            req = request.Request('https://api.zoomeye.org/host/search?query=ip:%s' % line.strip())
            req.add_header('Authorization', 'JWT '+access_token)
            with request.urlopen(req) as f:
                result = json.loads(f.read().decode('utf-8'))
                w.write(line.strip()+'\t'+str(result['total'])+'\n')
            line = r.readline()
        print('查询结束！')