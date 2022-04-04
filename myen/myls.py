from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader,RequestContext
from django.shortcuts import render
from django.views.decorators import csrf
import time
import os
import sqlite3
# Create your views here.

#带有用户登录，做题，保存记录 

def getml(wen):
    myml=os.getcwd()+"\\"+wen
    return(myml)

ml=getml("en.sqlite3")
def sql_ml(request):
   

    return render(request, 'myen/sql_ml.htm')

def sql_db(mysql):
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute(mysql)
    zd1=sj.fetchall()
    conn.commit()
    sj.close
    conn.close

    return zd1

def list_all(biaoming):
    zd={}
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute(biaoming)
    zd1=sj.fetchall()
    des = sj.description
    zd["tou"]=des
    zd["shuju"]=zd1
    sj.close 
    conn.close
    
    return zd
def sql_du(mysql):
    zd={}
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute(mysql)
    zd1=sj.fetchall()
    des = sj.description
    zd["tou"]=des
    zd["shuju"]=zd1
    sj.close 
    conn.close
    
    return zd

def sql_xie(mysql):
    #通用sql语句，无返回值,写入数据库
    zd=""
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute(mysql)
    conn.commit()

    sj.close 
    conn.close
    zd=mysql+"ok"
    return zd

def sj_du(request):
    ctx ={}
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute("select * from danci ORDER BY RANDOM() limit 20")
    zd1=sj.fetchall()
    des = sj.description
    ctx["tou"]=des
    ctx["shuju"]=zd1
    sj.close 
    conn.close
   

    return render(request, "myen/cs_list.htm", {"zd_list":ctx})




def chuti(lei,xueke):
    zd1=[]
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute("select * from timu  where leibie='"+ lei +"' and zhangjie ='"+xueke+"' ORDER BY RANDOM() limit 1")
    zd1=sj.fetchall()

    return zd1
def chuti_id(tm_id):
    zd1=[]
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute("select * from timu  where myid=" + tm_id)
    zd1=sj.fetchall()

    return zd1



def add_dan1(request):
    return render(request,"myen/ls_add_dan.html")
def add_dan2(request):
    timu1=[]
    timu2=[]
    zd={}
    jg=""
    if request.POST:
        xueke=request.POST['D1']
        shuru=request.POST['S1']
        zd["xk"]=xueke
        timu=fenge(shuru)
        for i in timu:
            tm_ls=i
            l=len(tm_ls)-1
            tm_ls[l]=str(tm_ls[l]).upper()
            tm_str="^".join(tm_ls)
            
            
            mysql="insert into lishi(leixing,timu,xueke) values('单选','{0}','{1}')".format(tm_str,xueke)
            print(mysql)
            jg=jg+sql_xie(mysql)+"<br>"
            # jg=jg+mysql+"<br>"
    return render(request,"myen/myshow.html",{"zd_list":jg})


def fenge(mystr):
    myok=[]
    gc=[]
    mystr=mystr.replace(',','，')
    mystr=mystr.replace('\'','’')
    mystr=mystr.replace('\"','“')
        
    mystr=mystr.replace('\r\n\r\n','^')
    gc=mystr.split('^')
    for i in gc:
        mystr1=i
        mystr1=mystr1.replace('\r\n','^')
        gc1=mystr1.split('^')
        myok.append(gc1)
   
    
    return myok

def timu_show(myid,mylei):
    if myid==0:
        mysql="select * from lishi where leixing='单选' "
        jieguo=sql_du(mysql)
    else:
        mysql="select * from lishi where myid={0}".format(myid)
        jieguo=sql_du(mysql)
        
       
        
    return jieguo

def timu1(request):
    tm_all=[]
    
    zd=timu_show(3,'单选')
    # ti=zd["shuju"]
    for i in zd["shuju"]:
        tm_list=[]
        ti_ls=i[2].split("^")
        tm_list.append(i[0])
        tm_list.append(ti_ls[0])
        for m in range(1,len(ti_ls)):
            tm_list.append(ti_ls[m])
        tm_all.append(tm_list)
        
    return render(request,"myen/testshow.html",{"zd_list":tm_all})
        
def timu2(request):
    if request.POST:
        xueke=request.POST.getlist("R1")
        
    
    
    return render(request,"myen/myshow.html",{"zd_list":xueke})
    
    


