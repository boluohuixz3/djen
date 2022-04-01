from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from django.shortcuts import render
from django.urls import reverse
from django.views import generic
import datetime

def runoobtime(request):
    import time
    zd={}
    zd["time"]=time.asctime()
    zd["tu"]="polls/images/2547.JPG"

    return render(request, "polls/runoobtime.html", {"zd_list": zd})

def runoobzd(request):
    import datetime
    zd={"姓名1":"赵","年龄1":15,"班级1":"3班"}
    zd["姓名2"]="钱"
    zd["年龄2"]=35
    zd["班级2"]="2班"

    #以字典方式返回
    return render(request, "polls/runoobzd.html", {"zd_list":zd})
#嵌套字典
def runoobzd2(request):
    import datetime
    jg={}
    zd={"姓名":"赵","年龄":15,"班级":"3班"}
    jg[1]=zd
    zd={"姓名":"钱","年龄":25,"班级":"4班"}
    jg[2]=zd
    zd={"姓名":"孙","年龄":35,"班级":"5班"}
    jg[3]=zd


    #以字典方式返回
    return render(request, "polls/runoobzd2.html", {"zd_list":jg})



def runooblist(request):
    import datetime
    zd=[]
    zd.append("钱")
    zd.append(35)
    zd.append("2班")

    #以列表方式返回,单层
    return render(request, "polls/runooblist.html", {"zd_list":zd})

def runooblist2(request):
    import datetime
    #中间列表注意清空
    l=[]
    zd=[]
    l.append("钱")
    l.append(35)
    l.append("2班")
    zd.append(l)
    l=[]
    l.append("孙")
    l.append(25)
    l.append("3班")
    zd.append(l)
    l=[]
    l.append("李")
    l.append(15)
    l.append("4班")
    zd.append(l)


    #以列表方式返回,多层
    return render(request, "polls/runooblist2.html", {"zd_list":zd})


def runoobdata(request):
    import time
    t1=time.time()
    import os
    import sqlite3
    zd1=[]
    conn=sqlite3.connect("gp.db") #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute("select * from xueji order by code limit 10000")
    zd1=sj.fetchall()
    t2=time.time()-t1
    td=[]
    td.append(t2)
    zd1.append(td)

    #以列表方式返回,单层
    return render(request, "polls/table.html", {"zd_list":zd1})

def runoobdata2(request):
    import time
    t1=time.time()
    import os
    import sqlite3
    zd1=[]
    conn=sqlite3.connect("gp.db") #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute("select * from xueji order by code limit 30000")
    zd1=sj.fetchall()
    t2=time.time()-t1
    td=[]
    td.append(t2)
    zd1.append(td)

    #以列表方式返回,单层
    return render(request, "polls/table.html", {"zd_list":zd1})


def tabledata(request):
    import time
    t1=time.time()
    import os
    import sqlite3
    jg={}
    zd1=[]
    conn=sqlite3.connect("gp.db") #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute("select count(*) from xueji ")
    zd1=sj.fetchall()
    jg["zongshu"]=zd1
    sj.execute("select count(*) from xueji where open<close ")
    zd1=sj.fetchall()
    jg["manzu"]=zd1
    sj.execute("select * from xueji where open<close  limit 1, 200")
    #筛选从第51之后50条数据
    jg["xianshi"]="51~100"
    zd1=sj.fetchall()
    jg["shuju"]=zd1
    jg["shijian"]=time.time()-t1
    des = sj.description
    jg["tou"]=des


    #以列表方式返回,单层
    return render(request, "polls/table2.html", {"zd_list":jg})

def tableday(request):
    import time
    t1=time.time()
    import os
    import sqlite3
    jg={}
    zd1=[]
    conn=sqlite3.connect("gp.db") #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute("select distinct(date) as riqi from xueji order by date desc")
    zd1=sj.fetchall()
    jg["shuju"]=zd1
   
    jg["shijian"]=time.time()-t1



    #以列表方式返回,单层
    return render(request, "polls/table3.html", {"zd_list":jg})

def tablecode(request):
    import time
    t1=time.time()
    import os
    import sqlite3
    jg={}
    zd1=[]
    conn=sqlite3.connect("gp.db") #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute("select distinct(code) as riqi from xueji order by code ")
    zd1=sj.fetchall()
    jg["shuju"]=zd1
   
    jg["shijian"]=time.time()-t1



    #以列表方式返回,单层
    return render(request, "polls/table4.html", {"zd_list":jg})

def myvote(request, question_id):
    return HttpResponse("You're voting on question 日期： %s." % question_id)


def daylist(request,question_id):
    import time
    t1=time.time()
    import os
    import sqlite3
    jg={}
    zd1=[]
    conn=sqlite3.connect("gp.db") #创建指定数据库 硬盘
    sj = conn.cursor()
#sj.execute("select code,open,close,low,high,volume,money from xueji where date='"+question_id+"' order by code")
    sj.execute("select * from xueji  where date='"+question_id+"'  order by code desc limit 1, 200")
    zd1=sj.fetchall()
    jg["shuju"]=zd1
    jg["shijian"]=time.time()-t1
    #jg["shijian"]=question_id
    des = sj.description
    jg["tou"]=des

    #以列表方式返回,单层
    return render(request, "polls/table2.html", {"zd_list":jg})

def codelist(request,question_id):
    import time
    t1=time.time()
    import os
    import sqlite3
    jg={}
    zd1=[]
    conn=sqlite3.connect("gp.db") #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute("select * from xueji where code='"+question_id+"' order by date desc")
    zd1=sj.fetchall()
    jg["shuju"]=zd1
    jg["shijian"]=time.time()-t1
    des = sj.description
    jg["tou"]=des

    #以列表方式返回,单层
    return render(request, "polls/table2.html", {"zd_list":jg})