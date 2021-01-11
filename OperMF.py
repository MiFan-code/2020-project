# -*- coding: utf-8 -*-
"""
因为每次修改ui，都需要将这个函数加进去，就很麻烦，所以就另外添加在这里了
另外完成一些显示工作
"""

from MF import *
import sys
import time
import stations
import dboper


def init_time(temp_ui):
    """
    将时间框里的时间调整
    :param temp_ui: MF中的Ui_MainWindow类
    :return:
    """
    localtime = time.localtime(time.time())
    init_year = localtime.tm_year
    init_month = localtime.tm_mon
    init_day = localtime.tm_mday
    temp_ui.dateEditForTrain.setDateTime(QtCore.QDateTime(QtCore.QDate(init_year, init_month, init_day), QtCore.QTime(0, 0, 0)))

def init_char(temp_ui):
    """
    设置初始的身份：成人
    :param temp_ui: MF中的Ui_MainWindow类
    :return:
    """
    temp_ui.ButtForAdult.click()

def init_tip(temp_ui):
    """
    初始化对白，根据时间
    22:00-5:00:夜深了，注意休息
    5:00-7:00：早晨好
    7；00-11:00：早上好
    11:00-13:00：中午好
    …
    :param temp_ui:  MF中的Ui_MainWindow类
    :return:
    """
    localtime=time.localtime(time.time())
    now_time=localtime.tm_hour
    if now_time>22 or now_time<=5:
        myTip="夜深了，注意休息"
    elif 5 < now_time <= 7:
        myTip="早!"
    elif 7<now_time<=11:
        myTip="早上好！"
    elif 11<now_time<=13:
        myTip="中午好！"
    elif 13<now_time<=18:
        myTip="下午好!"
    else:
        myTip="晚上好！"
    temp_ui.TipLabel.setText("呐！Master,"+myTip)

def init_icon(temp_app):
    """
    试图初始化任务栏的图表，但是貌似没什么用，罢了
    :param temp_app:
    :return:
    """
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("Icon/nf4~2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    temp_app.setWindowIcon(icon)


# 设置TableView
def Init_view(myUI):
    myUI.ShowTicket.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)#不可编辑
    myUI.ShowTicket.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)#垂直滚动条始终开启

"""
 def Query_click(self):
        Start_addre = self.start_in.text()
        Dict_addre = self.dict_in.text()
        Date_temp = self.dateEditForTrain.date()
        Date_year = str(Date_temp.year())
        Date_month = Date_temp.month()
        if Date_month < 10:
            Date_month = '0' + str(Date_month)
        else:
            Date_month = str(Date_month)
        Date_day = Date_temp.day()
        if Date_day < 10:
            Date_day = '0' + str(Date_day)
        else:
            Date_day = str(Date_day)
        Date = Date_year + '-' + Date_month + '-' + Date_day
        print(Start_addre + Dict_addre + Date)
        res = stations.query(Start_addre, Dict_addre, Date)
        print(res)
        if res == 1:
            self.TipLabel.setText("貌似有一些小问题，尝试再输入一遍吧")
        elif res == 2:
            self.TipLabel.setText("啧，没有可供选择的列车了呢，可能要考虑换乘了")
            self.ShowTicket.showRow(16)
        else:
            res = dboper.GetTrainInfo
            for temp in res:
                print(temp)
"""


def ui_opera():
    myApp = QtWidgets.QApplication(sys.argv)
    init_icon(myApp)
    myWindow = QtWidgets.QMainWindow()
    myUI = Ui_MainWindow()
    myUI.setupUi(myWindow)
    init_time(myUI)
    init_char(myUI)
    init_tip(myUI)
    Init_view(myUI)
    myUI.QueryButton.pressed.connect(myUI.Query_click)
    myWindow.show()
    sys.exit(myApp.exec_())


#是不是只看

