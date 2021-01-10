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
def queryout(station_name):
    try:
        conn = sqlite3.connect("stations.db")
        cursor = conn.cursor();
        quertorder = 'select * from all_station where name=\'' + station_name + '\''
        cursor.execute(quertorder)
        res = cursor.fetchone()
        finalres = res[1]
        cursor.close()
        conn.close()
    except (TypeError) as err:
        finalres="ERROR"
    return finalres

