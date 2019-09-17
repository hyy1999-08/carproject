import os
from flask import Flask, render_template, request, json, flash, redirect, jsonify
from werkzeug.utils import secure_filename
from aip import AipImageClassify
from help import get_file_content
from cheliang import *
import json
import time
import pymysql
from MYDB import MyDBHelper
from charge import *
from charge import chargefunction
# url="C:/Users/李祖荣憨憨/Desktop/License-Plate-Recognition-master(1)/License-Plate-Recognition-master/test/233.jpg"
# print(mypredict.getStr(url))
# list=mypredict.getStr(url)
# print(list[0])
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/yuyue')  # 页面链接该路由名称
def f_yuyue():
    return render_template("yuyue.html")

@app.route('/Index1')  # 页面链接该路由名称
def f_Index1():
    return render_template("Index1.html")

@app.route('/Index2')  # 页面链接该路由名称
def f_Index2():
    return render_template("Index2.html")
@app.route('/Register')  # 页面链接该路由名称
def f_register():
    return render_template("register.html")


@app.route('/login')  # 页面链接该路由名称
def f_login():
    return render_template("login.html")

@app.route('/logincheck',methods=['GET','POST'])
def logincheck():
    username = request.args.get("name")
    password = request.args.get("password")
    db = MyDBHelper()
    print(db.GetPassword(username))
    if(password==db.GetPassword(username)):
        print("ok")
        return json.dumps({'result': 'ok'})
    else:
        return json.dumps({'result': 'no'})


@app.route("/doregister", methods=['GET', 'POST'])
def doregister():
    username = request.args.get("name")
    password = request.args.get("password")
    print(username, password)
    db = MyDBHelper()
    args = [username, password]
    row = db.adduser(args)
    print("影响的行数", row)
    if row > 0:
        return json.dumps({'result': 'ok'})
    else:
        return json.dumps({'result': 'no'})


@app.route("/checkName", methods=['GET', 'POST'])
def checkName():
    username = request.args.get("name")
    print(username)
    db = MyDBHelper()
    username=db.GetUsername(username)
    if username.__len__() == 0:
        result = json.dumps({'result': 'ok'})
    else:
        result = json.dumps({'result': 'no'})
    return result

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        if os.path.exists("D:/CARS/"):
            file.save(os.path.join("D:/CARS/", filename))
            fileurl="D:/CARS/"+filename
            # time.strftime('%H:%M:%S', time.localtime(time.time()))
            strtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            APP_ID = '17061516'
            Type_client_id = '0aAPIpeYX7RbtFsEhSkzaFcY'
            Type_client_secret = 'W1jSIHOSa7zwVYnGyA2H4pmG3Y1tOpb1'
            get = get_type(fileurl)
            strtimefinal = datetime.datetime.strptime(strtime,'%Y-%m-%d %H:%M:%S')
            client = AipImageClassify(APP_ID, Type_client_id, Type_client_secret)
            image = get_file_content(fileurl)
            list=get_license_plate(fileurl)
            ctype = client.carDetect(image, options={"top_num": 1})["result"][0]["name"]
            db = MyDBHelper()
            db.addintime([strtimefinal, list])
            print(type(strtime))
            print(strtime)
            return jsonify({'str': list, 'time': strtime, 'type': ctype, "ctype": get})
        else:
            os.makedirs("D:/CARS/")
            file.save(os.path.join("D:/CARS/", filename))
            fileurl = "D:/CARS/" + filename
            get=get_type(fileurl)
            strtime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            strtimefinal=datetime.datetime.strptime(strtime,'%Y-%m-%d %H:%M:%S')
            print(type(strtime))
            APP_ID = '17061516'
            Type_client_id = '0aAPIpeYX7RbtFsEhSkzaFcY'
            Type_client_secret = 'W1jSIHOSa7zwVYnGyA2H4pmG3Y1tOpb1'

            client = AipImageClassify(APP_ID, Type_client_id, Type_client_secret)

            image = get_file_content(fileurl)
            list = get_license_plate(fileurl)
            ctype = client.carDetect(image, options={"top_num": 1})["result"][0]["name"]
            db = MyDBHelper()
            db.addintime([strtimefinal,list])
            print(strtime)
            return jsonify({'str': list, 'time': strtime, 'type': ctype,"ctype":get})
    return ''


@app.route('/uploadr/', methods=['GET', 'POST'])
def upload_r():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        if os.path.exists("D:/CARS/"):
            file.save(os.path.join("D:/CARS/", filename))
            fileurl = "D:/CARS/" + filename
            # time.strftime('%H:%M:%S', time.localtime(time.time()))
            strtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            APP_ID = '17061516'
            Type_client_id = '0aAPIpeYX7RbtFsEhSkzaFcY'
            Type_client_secret = 'W1jSIHOSa7zwVYnGyA2H4pmG3Y1tOpb1'
            get = get_type(fileurl)
            strtimefinal = datetime.datetime.strptime(strtime,'%Y-%m-%d %H:%M:%S')
            client = AipImageClassify(APP_ID, Type_client_id, Type_client_secret)
            image = get_file_content(fileurl)
            list = get_license_plate(fileurl)
            ctype = client.carDetect(image, options={"top_num": 1})["result"][0]["name"]
            db = MyDBHelper()
            db.addouttime([strtimefinal, list])
            print(type(strtime))
            print(strtime)
            return jsonify({'str': list, 'time': strtime, 'type': ctype, "ctype": get})
        else:
            os.makedirs("D:/CARS/")
            file.save(os.path.join("D:/CARS/", filename))
            fileurl = "D:/CARS/" + filename
            get = get_type(fileurl)
            strtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            strtimefinal = datetime.datetime.strptime(strtime,'%Y-%m-%d %H:%M:%S')
            str=strtime

            APP_ID = '17061516'
            Type_client_id = '0aAPIpeYX7RbtFsEhSkzaFcY'
            Type_client_secret = 'W1jSIHOSa7zwVYnGyA2H4pmG3Y1tOpb1'
            client = AipImageClassify(APP_ID, Type_client_id, Type_client_secret)
            image = get_file_content(fileurl)
            list = get_license_plate(fileurl)
            ctype = client.carDetect(image, options={"top_num": 1})["result"][0]["name"]
            db = MyDBHelper()
            db.addintime([strtimefinal, list])
            print(strtime)
            return jsonify({'str': list, 'time': strtime, 'type': ctype, "ctype": get})
    return ''

@app.route("/uploadsql/", methods=['GET', 'POST'])
def uploadsqlshow():
    carlicense=request.form.get("license")
    intime=request.form.get("intime")
    cartype=request.form.get("type")
    print(carlicense)
    print(intime)
    db=MyDBHelper()
    carexist=db.ecarlicense(carlicense)
    if carexist.__len__() == 0:
        args=[carlicense,intime,cartype]
        db.addcardatai(args)
        return jsonify({'result': 'ok', 'carlicense': carlicense, 'intime': intime, 'type': cartype})
    else:
        return jsonify({'result': 'no'})

@app.route("/uploadsqlr/", methods=['GET', 'POST'])
def uploadsqlrshow():
    if request.method == 'POST':
        carlicense=request.form.get("license")
        outtime=request.form.get("outtime")
        cartype=request.form.get("type")
        db=MyDBHelper()
        strtime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        carexist = db.ecarlicenseo(carlicense)
        if carexist.__len__() == 0:
            args = [carlicense, outtime, cartype]
            db.addcardatao(args)
            return jsonify({'result': 'ok', 'carlicense': carlicense, 'outtime': outtime, 'type': cartype})
        else:
            return jsonify({'result': 'no'})
    return ''

@app.route('/get_home')  # 页面链接该路由名称
def f_gethome():
    return render_template("function.html")
@app.route('/get_toshow')  # 页面链接该路由名称
def ftoshow():
    return render_template("toshow.html")
@app.route('/get_submitshow')  # 页面链接该路由名称
def f_getsubmitshow():
    return render_template("submitshow.html")
@app.route('/get_inshow')  # 页面链接该路由名称
def f_inshow():
    db = MyDBHelper()
    list = db.GetCarInfo()
    return render_template("inshow.html",list=list)

@app.route('/get_outshow')  # 页面链接该路由名称
def f_outshow():
    db = MyDBHelper()
    list = db.GetCarInfoout()
    return render_template("outshow.html",list=list)

@app.route('/get_useradd',methods=['GET','POST'])  # 页面链接该路由名称
def f_useradd():
    uname= request.form.get('uname')
    tell= request.form.get('tell')
    carplate = request.form.get('carplate')
    time = request.form.get('time')
    db = MyDBHelper()
    db.addyuyue([uname,tell,carplate,time])
    u=(uname,tell,carplate,time)
    return jsonify({'result':"ok"})

@app.route('/get_usershowfinal')  # 页面链接该路由名称
def f_usershowfinal():
    db = MyDBHelper()
    list=db.GetuserInfo()
    return render_template("usershow.html",list=list)
@app.route('/get_admit',methods=['GET','POST'])  # 页面链接该路由名称
def fgetadmit():
    uname=request.form.get('uname')
    db = MyDBHelper()
    db.deleteusershow(uname)
    return jsonify({'result':"ok"})
@app.route('/get_caramount/',methods=['GET','POST'])  # 页面链接该路由名称
def getcaramount():
    if request.method == 'POST':
        carmaxamount = request.form.get('maxamount')
        print(carmaxamount)
        print(type(carmaxamount))
        return jsonify({"carmaxamount":carmaxamount})
    return ""
UPLOAD_FOLDER = '/uploads'  #文件存放路径

if __name__ == '__main__':
    app.run(debug=True)
    UPLOAD_FOLDER = '/uploads'  # 文件存放路径
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
