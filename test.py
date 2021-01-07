'''
#这算是初学python的第一个程序吧
#加油！大作业！
#喜欢BMF，但是敲代码就要认真啊
@author:DDR
@test
'''
import flask
import random
import re
print("这是程序的开始");
height=float(input("请输入身高："));
if height>200:
    print("身高过高");
elif height<100:
    print("身高过矮");
else:
    print("还行");

number=no="这是一个假的变量";
#返回类型
print(type(no));
print(type(number));
#返回地址
print(id(no));
print(id(number));

no=20;
#返回类型
print(type(no));
print(type(number));
#返回地址
print(id(no));
print(id(number));

temp=4869;
print(temp);
#print("temp的值为"+temp);
print("转换为字符串输出："+str(temp));

msg="你的名字是世界上最短的祝福";
mdd="""期待一个有你的未来，
但是现在还是要好好努力""";
print(msg+'\n'+mdd);

print(621**2);
print(621//2);
print(621%2);
print(621/7);

print(str('a'>'b'));
print(str('a'>'b' or True));

passward=123456789;
passward=passward<<8;
print(passward);
print(passward/2**8);
passward=passward>>16;
print(passward);
passward=passward<<8;
print(passward);

num1=6;
num2=7;
if num1>num2:
    num3=num1;
else:
    num3=num2;
print(num3);
num3=num1 if num1<num2 else num2
print(num3);

#while语句循环
print("输出0到10之间的所有整数");
num=0
while num<=10:
    print(num);
    num+=1;
for num in range(0,10,3):
    print(num,end=' ');
print('\n');
for num1 in range(0,10,3):
    print("num1="+str(num1));
    for num2 in range(-10,10+1,5):
        if num2==0:
            continue;
        else:
            pass;
        print(num1*num2,end=' ');
    print('\n');

#索引和切片
verse=["但曾相见便相知","相见何如不见时","安得与君相决绝","免教生死作相思"];
print(verse*3);
for temp in verse:
    print(temp);
print(verse[0:3:2]);
emptylist=[None]*5;
print(emptylist);
print("何事秋风悲画扇" in verse);
print("但曾相见便相知" in verse);
print(len(verse));
apex=list(range(0,10,1));
print(apex);
apex=apex+verse;
print(apex);
apex=[list(range(0,10,1)),verse];
print(apex);
for index,item in enumerate(verse):
    print(index,item);
print("-----------");
verse.append("---固执着遥远的相守---");
for index,item in enumerate(verse):
    print(index,item);
anoverse=["人生若只如初见，何事秋风悲画扇","等闲变却故人心，却道故人心易变","骊山语罢清宵半，泪雨霖铃终不怨","何如薄幸锦衣郎，比翼连枝当日愿"];
verse.remove("---固执着遥远的相守---");
verse.extend(anoverse);
for index,item in enumerate(verse):
    print(index, item);
print(verse.count("人生若只如初见，何事秋风悲画扇"));

verse=[99,66,64,11,4,8,26];
print("verse元素的值之和为"+str(sum(verse)));
print("verse元素中的最大值为"+str(max(verse)));
versed=sorted(verse,reverse=True);
print("verse元素的降序排列为",versed);
versed=sorted(verse);
print("verse元素的升序排列为",versed);
verse.sort(reverse=True);
print("verse元素的值降序排列为",verse);
verse.sort();
print("verse元素升序排列为",verse);
del verse
verse=[random.randint(100,150) for temp in range(16)];
print(verse);
arr=[[i for i in range(-10,11,5)]for j in range(1,6,1)];
print(arr);
#元组
temp=tuple(range(-10,11,2));
print(temp);
temp2=(1,2,3,4,5,6,7,8,9);
print(temp2);
temp3=temp+temp2;
print(temp3);
temp4=((random.randint(120,150)for i in range(0,8,1))for t in range(0,8,1));
for cur in temp4:
    for ano in cur:
        print(ano,end=' ');
    print('\n');    

#字典
dictionary={"qq":"2563727655","ID":"别喂我橘子","用户姓名":"底德瑞"};
print(dictionary);
name=('王文','黄钧亭','颜弘宇','底德瑞');
address=['吉林','上海','福建','河北'];
dictionary=dict(zip(name,address));
print(dictionary);

#dictionary.clear();
test="底德瑞";
print(dictionary[test]if test in dictionary else "不在该字典内");
print(dictionary.get(test));
print(dictionary.items());
for item in dictionary.items():
    print(item);
dictionary["王逸轩"]="河北";
print(dictionary);

anodict={i:random.randint(10,100) for i in range(1,5)};
print(anodict);

#集合（set集合：最好的应用是去重）
aset={1,2,3,4,5,6};
print(aset);
anoset={random.randint(1000,9999)for i in range(0,6)}
print(anoset);
temp="2563727655";
temp2=set(temp);
print(temp2);
temp2.add('5');
print(temp2);
temp2.add("9");
print(temp2);

#字符串
verse="野渡无人舟自横";
byte=verse.encode("GBK");
print("原字符串：",verse);
print("转换后的字符串：",byte);
anoverse=byte.decode("GBK","strict");
print(anoverse);

str1="我的身高是：";
height=186;
str2="公分";
str3=str1+str(height)+str2;
print(str1+str(height)+str2);
str4=str3[0::2];
print(str4);

str5=str3.split('186');
print(str5);
str6='???'.join(str5);
print(str6);

numarr= [random.randint(0,9) for i in range(0,20)];
anostr=[];
trstr="";
for i in numarr:
    anostr.append(str(i));
    trstr=trstr+str(i);
    str7='@'.join(anostr);
for i in range(0,10):
    print("字符",i,"出现的次数为:",anostr.count(str(i)),end='****');
    print(i,"首次出现在的位置为",trstr.find(str(i)));
print(str7);
print(str7.replace('@',' '));

template="编号：%010d\t姓名：%s\t拼音：%s";
context=(729,"张嘉豪","zhangjiahao");
print(template%context);
#pause=input("只是暂停");

template="编号：{:0>10d}\t姓名：{:s}\t拼音：{:s}";
context=template.format(729,"张嘉豪","zhangjiahao");
print(context);

#使用正则表达式
pattern='mr_\n+';
print(pattern);
pattern=r'mr_\n+';
print(pattern);
pattern=r'mr_\w+';
string="MR_SHOP mr_shop";
match=re.match(pattern,string,re.I);
print(match);
anostring="项目的名字是MR_SHOP mr_shop";
match=re.match(pattern,string,re.I);
print(match);
print("匹配的起始位置为",match.start());
print("匹配的结束位置是",match.end());
print("匹配位置的元组是",match.span());
print("要匹配的字符串是",match.string);
print("匹配到的数据为",match.group());
match=re.search(pattern,anostring,re.I);
print(match);
print("匹配的起始位置为",match.start());
print("匹配的结束位置是",match.end());
print("匹配位置的元组是",match.span());
print("要匹配的字符串是",match.string);
print("匹配到的数据为",match.group());
match=re.findall(pattern,anostring,re.I);
print(match);

pattern=r'1[34567]\d{9}';
string='中奖号码为9999559 联系电话为15081441640,13780118077';
print_res=re.sub(pattern,'1??????????',string);
print(print_res);

pattern=r'[?|&]';
url='https://t.bilibili.com/?spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.27'
res=re.split(pattern,url);
print(res);