# -*- coding: utf-8 -*-
"""
# 从12306.cn中爬取数据，仅供学习用
# 网页更新之后需要改动stations.py中的url、车站文字代码匹配方式甚至更多
#pycharm中的pytho不允许语句之后分号结尾，强迫症表示很难受
#刚开始画UI的时候没考虑放缩的时候组建的位置和大小变化，画完之后才发现这个问题，积重难返了，干脆固定窗口大小
#虽然里面有文件操作和数据库操作，但是真正与项目有关的读写内容是通过数据库实现的，文件读写是测试时使用的。
@DDR WW
"""
import stations
import dboper
import OperMF

if __name__ == "__main__":
    stations.get_all_stations()
    temp = dboper.readout()
    stations.query("上海", "广州", "2021-06-16")
    res=dboper.GetTrainInfo()
    for all_train in res:
        print(all_train)
    OperMF.ui_opera()
