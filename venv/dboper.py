# -*- coding: utf-8 -*-
"""
将相关数据存入数据库sqlite3
"""
import sqlite3
import os
def FormMyDb(dictionary):
    """
    传入字典参数，构建数据库
    :return:
    """
    conn=sqlite3.connect("stations.db")
    cursor=conn.cursor()
    createorder='create table all_station(name varchar(20),nameid varchar(20))'
    cursor.execute(createorder)
    cursor.close()
    conn.close()
    conn = sqlite3.connect("stations.db")
    cursor = conn.cursor()
    for name,nameid in dictionary.items():
        addorder='insert into all_station (name,nameid) values ('+'\''+name+'\''+','+'\''+str(nameid)+'\''+')'
        #print(addorder)
        cursor.execute(addorder)
    cursor.close();
    conn.commit();
    conn.close();
def updatemydb(dictionary):
    DbTODel="stations.db"#如果存在之前的db文件，我们通过删除再重建的方式更新
    print(os.getcwd());
    if os.path.exists(DbTODel):
        os.remove(DbTODel)
       # print("删除成功")
    FormMyDb((dictionary));
def readout():
    conn=sqlite3.connect("stations.db")
    cursor=conn.cursor()
    cursor.execute('select * from all_station')
    res=cursor.fetchall()
    return res
def queryout(Key_value,getvalue=True):
    try:
        conn = sqlite3.connect("stations.db")
        cursor = conn.cursor();
        if getvalue:
            quertorder = 'select * from all_station where name=\'' + Key_value + '\''
            cursor.execute(quertorder)
            res = cursor.fetchone()
            finalres = res[1]
        else:
            quertorder = 'select * from all_station where nameid=\'' + Key_value + '\''
            cursor.execute(quertorder)
            res = cursor.fetchone()
            finalres = res[0]
        cursor.close()
        conn.close()
    except (TypeError) as err:
        finalres="ERROR"
    return finalres

def FormTrainInfo(FromatInfo):
    DbTODel = "TrainInfo.db"  # 如果存在之前的db文件，我们通过删除再重建的方式更新
    print(os.getcwd());
    if os.path.exists(DbTODel):
        os.remove(DbTODel)
    # print("删除成功")
    conn = sqlite3.connect("TrainInfo.db")
    cursor = conn.cursor()
    """
                    车次编号：第三栏
                    出发站：第四栏
                    到达站：第七栏
                    发时：第八栏
                    到时：第九栏
                    历时：第十栏
                    商务座特等座：第32栏
                    一等座：第31栏
                    二等（包）座：第30栏
                    高级软卧：第21栏
                    软卧：第23栏
                    动卧：第33栏
                    硬卧：第28栏
                    软座：第24栏
                    硬座：第29栏
                    无座：第26栏
                    其他：
                """
    createorder = 'create table res_train(v_name varchar(20),start_sta varchar(20), dict_sta varchar(20),start_time varchar(20),get_time varchar(20),period varchar(20),busn_seat varchar(20),Fir_seat varchar(20),sec_seat varchar(20),sup_soft_bed varchar(20),soft_bed varchar(20),move_bed varchar(20),hard_bed varchar(20),soft_seat varchar(20),hard_seat varchar(20),no_seat varchar(20))'
    print(createorder)
    cursor.execute(createorder)
    cursor.close()
    conn.close()
    conn = sqlite3.connect("TrainInfo.db")
    cursor = conn.cursor()
    for signal_info in FromatInfo:
        addorder="insert into res_train(v_name,start_sta,dict_sta,start_time,get_time,period,busn_seat,Fir_seat,sec_seat,sup_soft_bed,soft_bed,move_bed,hard_bed,soft_seat,hard_seat,no_seat) values ("

        for item in signal_info:
            addorder=addorder+item+','
        addorder=addorder[0:len(addorder)-1]
        addorder=addorder+')'
        print(addorder)
        cursor.execute(addorder)
    cursor.close();
    conn.commit();
    conn.close();
    print("已将车次信息存放到数据库中")

def GetTrainInfo():
    conn=sqlite3.connect("TrainInfo.db")
    cursor=conn.cursor()
    myOrder='select * from res_train'
    cursor.execute(myOrder)
    res=cursor.fetchall()
    cursor.close()
    conn.close
    return res