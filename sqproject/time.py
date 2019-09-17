#-*- coding: utf-8 -*-
#!/usr/bin/env python
#from aip import AipImageClassify
import urllib
import urllib.parse
import urllib.request
import base64
import json
import time
import pymysql
from charge import chargefunction

conn = pymysql.connect(
        host="cdb-5dbx2bwu.bj.tencentcdb.com",
        port=10113,
        db="carproject",
        user="root",
        password="Favc0812",
        charset="utf8"
    )


def addplate(args):
    # 1.建立连接
    '''conn = pymysql.connect(
        host="cdb-5dbx2bwu.bj.tencentcdb.com",
        port=10113,
        db="carproject",
        user="root",
        password="Favc0812",
        charset="utf8"
    )'''
    # 2.创建游标
    cs = conn.cursor()
    # 3.执行sql语句
    print(args)
    row = cs.execute("INSERT INTO time_test (carplate,recogtime) values(%s,%s)", args)
    conn.commit()
    return row


Plate_client_id= 'Ai2Cu96XhA7W0ahYEPmHiLVm'
Plate_client_secret = '6pgQIjByedcaHfe8zZqEwi7tIdYHxKlb'
#APP_ID='17061516'
#Type_client_id = '0aAPIpeYX7RbtFsEhSkzaFcY'
#Type_client_secret = 'W1jSIHOSa7zwVYnGyA2H4pmG3Y1tOpb1'
#client=AipImageClassify(APP_ID,Type_client_id,Type_client_secret)
# 获取token
def get_token_plate():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + Plate_client_id + '&client_secret=' + Plate_client_secret
    request = urllib.request.Request(host)
    request.add_header('Content-Type','application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    token_content = response.read()
    if token_content:
        token_info = json.loads(token_content.decode("utf-8"))
        token_key = token_info['access_token']
    return token_key


# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 获取车牌号信息
recogtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
def get_license_plate(path):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"
    global number
    f = get_file_content(path)
    access_token = get_token_plate()
    img = base64.b64encode(f)
    params = {"custom_lib": False, "image": img}
    params = urllib.parse.urlencode(params).encode('utf-8')
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        license_plates = json.loads(content.decode("utf-8"))
        strover = '识别结果：'
        words_result = license_plates['words_result']
        number = words_result['number']
        strover += '{} \n '.format(number)
        #print (content)
        print(strover)
        return content
    else:
        return ''

'''
def get_car_type(path):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"

    f = get_file_content(path)
    access_token = get_token_type()
    img = base64.b64encode(f)
    params = {"custom_lib": False, "image": img}
    params = urllib.parse.urlencode(params).encode('utf-8')
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        license_plates = json.loads(content.decode("utf-8"))
        strover = '识别结果：'
        words_result = license_plates['words_result']
        number = words_result['number']
        strover += '  车牌号：{} \n '.format(number)
        #print (content)
        print(strover)
        return content
    else:
        return ''
'''
def typeof(variate):
    type=None
    if isinstance(variate,int):
        type = "int"
    elif isinstance(variate,str):
        type = "str"
    elif isinstance(variate,float):
        type = "float"
    elif isinstance(variate,list):
        type = "list"
    elif isinstance(variate,tuple):
        type = "tuple"
    elif isinstance(variate,dict):
        type = "dict"
    elif isinstance(variate,set):
        type = "set"
    return type

image_path = "D:/CARS/20190822112113.jpg"
data=get_license_plate(image_path)
print(recogtime)

#读取数据库中识别车牌号的时间信息
cursor = conn.cursor()
sql = "SELECT entertime,leavetime FROM time_test WHERE carplate = %(name)s" % {"name":data}
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表3
    time_tuple = cursor.fetchone()
    #print(entertime_tuple)
    entertime = time_tuple[0]
    leavetime = time_tuple[1]
    print(entertime)
    print(leavetime)
    vartype1 = typeof(entertime)
    print(vartype1)


except:
   print ("Error: unable to fetch data")

abc=typeof(sql)
print(abc)

#判断语句，决定功能
if sql is None:
    entertime = recogtime
    args = [number, entertime]
    addplate(args)
    print("进入时间" + entertime)
else:
    print("祝您一路平安")
    leavetime = recogtime
    vartype2 = typeof(leavetime)
    chargefunction(entertime, leavetime)
