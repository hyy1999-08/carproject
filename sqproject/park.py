import pymysql

max_car = 5
car_lst = []

def adduser(args):
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
    row = cs.execute("INSERT INTO park(platenumber,cur_park,park_in) values(%s,%s,%s)", args)
    conn.commit()
    return row

def getplate(self,args):
    return args
class car():
    def __init__ (self, platenumber):
        self.platenumber = platenumber

    def park(self):
        if len(car_lst)<max_car:
            park_in = 1
            car_lst.append(self)
            cur_park = max_car - len(car_lst)
            print("停车成功。当前剩余车位：")
            print(cur_park)
            args=[pla,cur_park,park_in]
            adduser(args)

        else:

            print("车库已满")

    def exit(self):
        cur_car = len(car_lst)-1 if len(car_lst) == max_car else  len(car_lst)
        #print("运行")
        for i in range(0, cur_car):
            #print(i)
            #print("self:"+self.platenumber)
            #print("car_list:"+car_lst[i].platenumber)
            if car_lst[i].platenumber == self.platenumber:
                park_in = 0
                car_lst.remove(car_lst[i])
                cur_park = max_car-len(car_lst)
                print("出车成功。当前剩余车位：")
                print(cur_park)
                args=[pl,cur_park,park_in]
                adduser(args)
                return
            else:
                print("该汽车从未进入车库，请与管理员联系。")
