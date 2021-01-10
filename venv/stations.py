# -*- coding: utf-8 -*-
import requests
import re
import os
#import fileoper
import dboper

def get_all_stations():
    tarurl="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9181";#这个地址是会变的，现在我还不会自动获取，只能通过维护和更新
    response=requests.get(tarurl);
    # 就是说，分析html之后，我们发现只要匹配的（【汉字车站名】+‘|’+（英文代号））
    station_name=re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text);
    names=dict((station_name));#转换成字典
    all_name=str(names);
#    fileoper.writein('stations.txt',all_name,'utf-8');
    dboper.updatemydb(names)

