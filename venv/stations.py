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
    response.close()
    names=dict((station_name));#转换成字典
    all_name=str(names);
#    fileoper.writein('stations.txt',all_name,'utf-8');
    dboper.updatemydb(names)
def query(start_sta,dict_sta,start_time,is_adult=True):
    """
    通过信息爬取票务信息
    :param start_sta: string 出发地
    :param dict_sta:  string 目的地
    :param start_time: string 例如‘2021-1-11’ 出发时间
    :param is_adult: Boolean 是否为成人票，默认成人票
    :return:
    """
    start_id=dboper.queryout(start_sta)
    dict_id=dboper.queryout(dict_sta)
    #print(start_id,' ',dict_id)
    if is_adult:
        purpose='ADULT'
    else:
        purpose="0X00"
    #合成出目标网址，如果不能查询，说明不能购票
    tarurl="""https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date="""+start_time+"""&leftTicketDTO.from_station="""+start_id+"""&leftTicketDTO.to_station="""+dict_id+"""&purpose_codes="""+purpose
    print(tarurl)
    #如果response的返回网址为https://www.12306.cn/mormhweb/logFiles/error.html，说明出现了错误
    ErrorUrl='https://www.12306.cn/mormhweb/logFiles/error.html'
    anourl="https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date=2021-01-11&leftTicketDTO.from_station=TJP&leftTicketDTO.to_station=SHH&purpose_codes=0X00"
    header={"User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 Edg/87.0.664.75'}
    cookie={'_uab_collina':'161025819101751929999494','JSESSIONID':'E270F94B5EC67B0684D0E1E58642450F','RAIL_DEVICEID':'IqK1TZStsEdUI9H3e9ZRgY6OcEwfwfotTCST3gfGcwBYqy3wB3P9eSBl1Z5R5jsXnenK75t8WfC0FMlcdmH1xnrLt5sls15R4JiMSoJioSGdelp4bsX-rW487E9ijP3u7TTLAyyEDxVJAkHxekfZAbAQ5MyswIDm'}
    response = requests.get(tarurl,headers=header,cookies=cookie)
    ErrorTag=-1;
    if response.url==ErrorUrl:
        ErrorTag=1
        #出错处理
    #果不是错误信息
    else:
        res_js = response.json()
        #print(res_js)
        draft_data=res_js['data']['result']
        if len(draft_data)==0:
            ErrorTag=2
        else:
            print(draft_data)
            draft_ano_data=[]
            fromat_list=[]
            for temp in draft_data:
                print(temp)
                train_list=temp.split('|')
                num=0
                for nnnn in train_list:
                    num+=1
                print("共分成了",num,"栏");
                #不能买票的话，就不看他
                if train_list[11]!='IS_TIME_NOT_BUY':
                    draft_ano_data.append(train_list)
                    print("暂存，待处理")
                else:
                    print("移除，不显示")
            for temp in draft_ano_data:
                print('\n')
                num=0
                train_info=[];
                for anotemp in temp:
                    print("第",num,"栏：",anotemp,end='')
                    num+=1;
                Useful_info=[3,4,7,8,9,10,32,31,30,21,23,33,28,24,29,26]
                site=[0,1,2,3,4,5,14,13,12,6,7,15,10,8,11,9]
                title=["车次","出发站","到达站","出发时间","到达时间","用时","商务座","一等座","二等座","高级软卧","软卧","动卧","硬卧","软座","硬座","无座"]
                temptitle=[]
                for i in title:
                    temptitle.append('\''+i+'\'')
                fromat_list.append(temptitle)
                for index in Useful_info:
                    if index!=4 and index!=7:
                        if temp[index]=='':
                            temp[index]='--'
                        train_info.append('\''+temp[index]+'\'')
                    else:
                        train_info.append('\'' + dboper.queryout(temp[index],False) + '\'')#得到代号所对应的车站名
                """
                    if num-1 in Useful_info:
                        if num-1!=4 and num-1!=7:
                            if anotemp=='':
                                anotemp='--'
                            train_info.append('\''+anotemp+'\'')
                        else:
                            train_info.append('\'' + dboper.queryout(anotemp,False) + '\'')#得到代号所对应的车站名
                """
                print(train_info,len(train_info))
                fromat_list.append(train_info)
            dboper.FormTrainInfo(fromat_list)#将整理好的信息发送到数据库
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
    return ErrorTag




