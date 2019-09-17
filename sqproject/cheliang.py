# encoding:utf-8
import base64
import urllib
import urllib.request
import sys
import ssl
import json

'''
车辆分析—车辆属性识别
'''

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_token_type():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=4fx8H0O4oZom6COGMG4p8v6G&client_secret=XB5e4GI5sF6yjD84S5o8PvqOcYQpRFv0'
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    token_content = response.read()
    if token_content:
        token_info = json.loads(token_content.decode("utf-8"))
        token_key = token_info['access_token']
    return token_key

def get_token_plate():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Ai2Cu96XhA7W0ahYEPmHiLVm&client_secret=6pgQIjByedcaHfe8zZqEwi7tIdYHxKlb'
    request = urllib.request.Request(host)
    request.add_header('Content-Type','application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    token_content = response.read()
    if token_content:
        token_info = json.loads(token_content.decode("utf-8"))
        token_key = token_info['access_token']
    return token_key

def get_type(path):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_attr"
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
        information= json.loads(content.decode("utf-8"))
        #print("information:",information)
        value1 = information.get('vehicle_info')
        #print("value1:",value1)
        value2 = value1[0]
        #print("value2:",value2)
        value3 = value2.get('attributes')
        #print("value3:",value3)
        value4 = value3.get('vehicle_type')
        #print("value4:",value4)
        value5 = value4.get('name')
        print("汽车类型：",value5)
        return value5
    else:
        return ''


def get_license_plate(path):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"

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
        # print(license_plates)
        value1 = license_plates.get('words_result')
        # print(value1)
        number = value1.get('number')
        print(number)
        return number
    else:
        return ''

