import pymysql
from charge import*
class MyDBHelper:
# -*-coding:utf-8 -*-

    def GetCarInfo(self):
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        cs = conn.cursor()
        password = cs.execute("SElECT * FROM cardataini")
        password = cs.fetchall()
        conn.commit()
        return password

    def GetCarInfoout(self):
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        cs = conn.cursor()
        password = cs.execute("SElECT * FROM cardataout")
        password = cs.fetchall()
        conn.commit()
        return password
    def GetuserInfo(self):
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        cs = conn.cursor()
        password = cs.execute("SElECT * FROM userdata")
        password = cs.fetchall()
        conn.commit()
        return password

    def GetPassword(self,name):
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        cs = conn.cursor()
        password = cs.execute("SElECT * FROM submits WHERE username=%s", name)
        password=cs.fetchall()
        conn.commit()
        return password[0][2]

    def GetUsername(self,name):
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        cs = conn.cursor()
        username = cs.execute("SElECT * FROM submits WHERE username=%s", name)
        username = cs.fetchall()
        conn.commit()
        return username

    def ecarlicense(self,carplate):
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        cs = conn.cursor()
        eamount = cs.execute("SElECT * FROM cardataini WHERE carplate=%s",carplate)
        eamount = cs.fetchall()
        conn.commit()
        return eamount
    def yuyueamount(self):
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        cs = conn.cursor()
        eamount = cs.execute("SELECT COUNT(uname) FROM userdata")
        return eamount

    def ecarlicenseo(self,carplate):
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        cs = conn.cursor()
        eamount = cs.execute("SElECT * FROM cardataout WHERE carplate=%s",carplate)
        eamount = cs.fetchall()
        conn.commit()
        return eamount
    def chargefunction(self,carplate):

            conn = pymysql.connect(
                host="cdb-5dbx2bwu.bj.tencentcdb.com",
                port=10113,
                db="carproject",
                user="root",
                password="Favc0812",
                charset="utf8"
            )
            cs = conn.cursor()
            intime = cs.execute("SElECT intime FROM intime WHERE carplate=%s",carplate)
            outtime=cs.execute("SElECT outtime FROM outtime WHERE carplate=%s",carplate)
            money=chargefunction(intime,outtime)
            conn.commit()
            return money


    def Carplatenumber(self,name):
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        cs = conn.cursor()
        username = cs.execute("SElECT * FROM cardata WHERE username=%s", name)
        username = cs.fetchall()
        conn.commit()
        return username


    def CreateDatabase(self,sql):
            db = pymysql.connect(
                host="cdb-5dbx2bwu.bj.tencentcdb.com",
                port=10113,
                db="carproject",
                user="root",
                password="Favc0812",
                charset="utf8"
            )
            cursor = db.cursor()
            cursor.execute(sql)
            print("成功")
            db.close()

    def CreateTable(self,databasename):
            cars=pymysql.connect(
                host="cdb-5dbx2bwu.bj.tencentcdb.com",
                port=10113,
                password="Favc0812",
                user="root",
                db=databasename
            )



    # def  addcar(self,args):
    #             conn = pymysql.connect(
    #                 host="localhost",
    #                 port=3306,
    #                 db="cars",
    #                 user="root",
    #                 password="123456",
    #                 charset="utf8"
    #                  )
    #             cs=conn.cursor()
    #             sql="INSERT INTO cardata values (null,%s) "
    #             row=cs.execute(sql,args)
    #             conn.commit()
    #             return row

    def  adduser(self,args):
        # 1.建立连接
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        # 2.创建游标
        cs = conn.cursor()
        # 3.执行sql语句
        print(args)
        row = cs.execute("INSERT INTO submits (username,password) values(%s,%s)",args)
        conn.commit()
        return row


    def addinresult(self, args):
        # 1.建立连接
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        # 2.创建游标
        cs = conn.cursor()
        # 3.执行sql语句
        print(args)
        row = cs.execute("INSERT INTO inresult (carplate,intime,type) values(%s,%s,%s)", args)
        conn.commit()
        return row
    def addoutresult(self, args):
        # 1.建立连接
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        # 2.创建游标
        cs = conn.cursor()
        # 3.执行sql语句
        print(args)
        row = cs.execute("INSERT INTO outresult (carplate,outtime,type) values(%s,%s,%s)", args)
        conn.commit()
        return row
    def addmyuser(self, args):
        # 1.建立连接
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        # 2.创建游标
        cs = conn.cursor()
        # 3.执行sql语句
        print(args)
        row = cs.execute("INSERT INTO submits (username,password) values(%s,%s)", args)
        conn.commit()
        return row
    def addintime(self, args):
        # 1.建立连接
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        # 2.创建游标
        cs = conn.cursor()
        # 3.执行sql语句
        print(args)
        row = cs.execute("INSERT INTO intime (intime,carplate) values(%s,%s)", args)
        conn.commit()
        return row
    def addouttime(self, args):
        # 1.建立连接
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        # 2.创建游标
        cs = conn.cursor()
        # 3.执行sql语句
        print(args)
        row = cs.execute("INSERT INTO outtime (outtime,carplate) values(%s,%s)", args)
        conn.commit()
        return row
    def addcar(self,args):
        # 1.建立连接
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        # 2.创建游标
        cs = conn.cursor()
        print(args)
        row = cs.execute("INSERT INTO cardata  (outime,amount) values(%s,%s,%s,%d)", args)
        conn.commit()
        return row
#进来时传进来两个值
    def  addcardatai(self,args):
        # 1.建立连接
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        # 2.创建游标
        cs = conn.cursor()
        print(args)
        row=cs.execute("INSERT INTO cardataini (carplate,intime,ctype) values(%s,%s,%s)",args)
        conn.commit()
        return row
    def  addcardatao(self,args):
        # 1.建立连接
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        # 2.创建游标
        cs = conn.cursor()
        print(args)
        row=cs.execute("INSERT INTO cardataout (carplate,outtime,ctype) values(%s,%s,%s)",args)
        conn.commit()
        return row
    def  addyuyue(self,args):
        # 1.建立连接
        conn = pymysql.connect(
            host="cdb-5dbx2bwu.bj.tencentcdb.com",
            port=10113,
            db="carproject",
            user="root",
            password="Favc0812",
            charset="utf8"
        )
        # 2.创建游标
        cs = conn.cursor()
        print(args)
        row=cs.execute("INSERT INTO userdata (uname,tell,carplate,time) values(%s,%s,%s,%s)",args)
        conn.commit()
        return row
    def deletecardatain(self,carplate):
        # 1.建立连接
        try:
            conn = pymysql.connect(
                host="cdb-5dbx2bwu.bj.tencentcdb.com",
                port=10113,
                db="carproject",
                user="root",
                password="Favc0812",
                charset="utf8"
            )
            # 2.创建游标
            cs = conn.cursor()
            row =cs.execute("delete from cardataini where carplate=%s",[carplate])
            print(row)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
               conn.close()
    def deleteusershow(self,uname):
        # 1.建立连接
        try:
            conn = pymysql.connect(
                host="cdb-5dbx2bwu.bj.tencentcdb.com",
                port=10113,
                db="carproject",
                user="root",
                password="Favc0812",
                charset="utf8"
            )
            # 2.创建游标
            cs = conn.cursor()
            row =cs.execute("delete from userdata where uname=%s",[uname])
            print(row)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
               conn.close()
    def deletecardataout(self,carplate):
        # 1.建立连接
        try:
            conn = pymysql.connect(
                host="cdb-5dbx2bwu.bj.tencentcdb.com",
                port=10113,
                db="carproject",
                user="root",
                password="Favc0812",
                charset="utf8"
            )
            # 2.创建游标
            cs = conn.cursor()
            row =cs.execute("delete from cardataout where carplate=%s",[carplate])
            print(row)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
               conn.close()

#统计数据
    def showcardatain(self, id):
        try:
            conn = pymysql.connect(
                host="cdb-5dbx2bwu.bj.tencentcdb.com",
                port=10113,
                db="carproject",
                user="root",
                password="Favc0812",
                charset="utf8"
            )
            cs = conn.cursor()
            cs.execute("select * from  cardataini ", [id])
            result = cs.fetchall()
            count=cs.execute("SELECT  COUNT(carplate) FROM  table_name")
            #计算记录数
            return result
        except Exception as e:
            print(e)
        finally:
            if conn != None:
                conn.close()
#统计数据
    def showcardataout(self, id):
        try:
            conn = pymysql.connect(
                host="cdb-5dbx2bwu.bj.tencentcdb.com",
                port=10113,
                db="carproject",
                user="root",
                password="Favc0812",
                charset="utf8"
            )
            cs = conn.cursor()
            cs.execute("select * from cardataini ", [id])
            result = cs.fetchall()
            count=cs.execute("SELECT  COUNT(carplate) FROM  table_name")
            #计算记录数
            return {"result":result,"count":count}
        except Exception as e:
            print(e)
        finally:
            if conn != None:
                conn.close()

    #def delete(self, id):
    #        try:
    #            conn = pymysql.connect(
    #                host="localhost",
    #                port=3306,
    #                db="cars",
    #                user="root",
    #                password="123456",
    #                charset="utf8"
    #            )
    #            cs = conn.cursor()
    #            row = cs.execute("delete from myuser where uid=%s", [id])
    #            print(row)
    #            conn.commit()
    #        except Exception as e:
    #            print(e)
    #        finally:
    #            if conn is not None:
    #                conn.close()d
