#coding=utf-8
import urllib, urllib2, sys
import ssl,base64

#  client_id 为官网获取的AK， client_secret 为官网获取的SK
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

access_token = token_temp2
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
# �����Ʒ�ʽ��ͼ�ļ�
f = open(r'E:\mgliu\20180620153758.jpg', 'rb')
# ����image��ͼ��base64����
img = base64.b64encode(f.read())
params = {"image": img}
params = urllib.urlencode(params)
request = urllib2.Request(url, params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)