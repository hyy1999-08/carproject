
# -*-coding:utf-8 -*-

import pymysql

class CreateDatabase():
    def __init__(self,sql):
        db=pymysql.connect(
            host="localhost",
            port=3306,
            password="200152523",
            user="root",
            )

        cursor=db.cursor()
        cursor.execute(sql)
        print("成功")
        db.close()
if __name__=='__main__':
    test=CreateDatabase("create database gg")
