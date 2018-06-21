#coding=utf-8
'''
Created on 2018年6月20日

@author: mgliu
'''

if __name__ == '__main__':
    pass

import urllib, urllib2, sys
import ssl,base64

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=k0QbFfnaPw2xvjgIj5rGcUP2&client_secret=H9WCVnh2xM0kzjigkl9SS8CKKhOLsOgg'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)
temp_content= eval(content);
#token_temp=content['access_token'];
token_temp2=temp_content.get('access_token')
print (token_temp2)


access_token = token_temp2;
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/idcard?access_token=' + access_token
# 二进制方式打开图文件
f = open(r'E:\mgliu\20180620145737.jpg', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
params = {"image": img, "id_card_side": "front","detect_direction":"true","detect_risk":"true"}
params = urllib.urlencode(params)
request = urllib2.Request(url, params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)
    
print type(content)
temp_card_result=eval(content);
user_name=temp_card_result['words_result']['姓名']['words']
card_no=temp_card_result['words_result']['公民身份号码']['words']
user_addr=temp_card_result['words_result']['住址']['words']

print (user_name)
print(card_no)
print(user_addr)
