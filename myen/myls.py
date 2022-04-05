
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
    tou=[]
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute(biaoming)
    zd1=sj.fetchall()
    des = sj.description
    for i in des:
        print(i)
        tou.append(i[0])
    zd["tou"]=tou
    zd["shuju"]=zd1
    sj.close 
    conn.close
    
    return zd
def sql_du(mysql):
    zd={}
    tou=[]
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute(mysql)
    zd1=sj.fetchall()
    # des = sj.description
    # for i in des:
    #     tou.append(i[0])
    # zd["tou"]=tou
    
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

def timu1(request):
    jieguo=[]
    zz2=request.GET.get('user_id')
    zz1=request.GET.get('timu_id')
    zz3=request.GET.get('jl_id')
    if int(zz1)<1 :
        jilu=chuti1(zz2,0)
        # print("jilu:",jilu)
        jieguo=timu_show(jilu[1])
        jieguo.append(zz2)
        jieguo.append(jilu[0])
    else:
        jieguo=timu_show(zz1)
        
        jieguo.append(zz2)
        jieguo.append(zz3)
            
       
        
    return render(request,"myen/testshow.html",{"zd_list":jieguo}) 

def timu_show(timu_id):
    jieguo=[]
    i=[]
    mysql="select * from lishi where myid={0}".format(timu_id)
    print(mysql)
    zd=sql_du(mysql)["shuju"]
    if len(zd)>0:
        print(zd)
        i = zd[0]
        jieguo=i[2].split("^")
        jieguo.insert(0,i[0])
    
        
    return jieguo
        
def timu2(request):
    jieguo={}
    tm_ls=[]
    if request.POST:
        zz2=request.GET.get('user_id')
        zz1=request.GET.get('timu_id')
        zz3=request.GET.get('jl_id')
        xueke=request.POST["R1"]
        xuanze=chr(62+int(xueke))
        tm_ls=timu_show(zz1)
        jieguo["timu"]=tm_ls
        jieguo["user_id"]=zz2
        jieguo["xuanze"]=xuanze
        jieguo["timu_id"]=zz1
        jieguo['jilu_id']=zz3
        print(tm_ls[6])
        if tm_ls[6]==xueke:
            defen=1
        else:
            defen=0
        mysql="update jilu set daan='{0}',defen='{2}' where myid={1}".format(xueke,zz3,defen)
        a=sql_xie(mysql)
        new_tm=chuti1(zz2,0)
        if len(new_tm)==0:
            jieguo["jiesu"]=0
        else:
            jieguo['jiesu']=new_tm[1]
        
        
    return render(request,"myen/testout.html",{"zd_list":jieguo})    
    
    
def userload(request):
        
   
    return render(request,"myen/index.html",{"zd_list":"请选择班级和姓名"})
    
def userload2(request):
    jieguo=[]
    tm_ls=[]
    if request.POST:
        banji=request.POST["D1"]
        xingming=request.POST["T1"]
        if xingming=="":
            chu="姓名必须输入"
            return render(request,"myen/index.html",{"zd_list":chu})
        t0=time.time()
        mysql="select * from denglu where banji='{0}' and xingming='{1}' order by myid desc".format(banji,xingming)
        user_id=sql_du(mysql)["shuju"]
                
        if len(user_id)>0:
            load_id=user_id[0][0]
            mysql="update denglu set shijian='{0}',jiesu='0' where myid={1} ".format(t0,load_id)
            # chu=mysql
            chu=sql_xie(mysql)
            chu=shaixun(load_id,30)
            tm_ls=chuti1(load_id,0)
            jieguo=timu_show(tm_ls[1])
            jieguo.append(load_id)
            jieguo.append(tm_ls[0])
            chu=jieguo
            
            
        else:
                
            mysql="insert into denglu(banji,xingming,shijian,jiesu) values('{0}','{1}','{2}','{3}')".format(banji,xingming,t0,'0')
            # chu=mysql
            chu=sql_xie(mysql)
            mysql="select * from denglu where banji='{0}' and xingming='{1}' order by myid desc".format(banji,xingming)
            user_id=sql_du(mysql)["shuju"]
            chu1=user_id[0][0]
            chu=shaixun(chu1,30)
            tm_ls=chuti1(load_id,0)
            jieguo=timu_show(tm_ls[1])
            jieguo.append(load_id)
            jieguo.append(tm_ls[0])
            chu=jieguo
            
        

    return render(request,"myen/testshow.html",{"zd_list":chu})

def shaixun(user_id,shu):
    mysql="delete  from jilu  where user_id={0}".format(user_id)
    tm_str=sql_xie(mysql)
    tm_list=sql_du(mysql)["shuju"]
    mysql="select myid from lishi  ORDER BY  RANDOM()  limit {0}".format(shu)
    
    tm_list=sql_du(mysql)["shuju"]
    n=1
    for i in tm_list:
        
        mysql="insert into jilu(user_id,timu,jielun) values('{0}','{1}','{2}')".format(user_id,i[0],n)
        # print(mysql)
        sql_xie(mysql)
        n=n+1
    jieguo="ok"
    
    
    return jieguo

def chuti1(user_id,tm_id):
    jieguo=[]
    if tm_id==0:
        mysql="select myid,timu from jilu where user_id='{0}' and daan= '^'".format(user_id)
        print(mysql)
        timu=sql_du(mysql)["shuju"]
        # print("timu:",timu[0])
        
        # timu=timu
        # print(timu[0])
        
    else:
        # mysql="select myid,timu from jilu where user_id='{0}' and daan= '^'".format(user_id)
        # timu=sql_du(mysql)["shuju"]
        print("timu:",timu[0])
        
        # timu=timu
        # print(timu[0])
    jieguo=timu[0]
    return jieguo

def timushowall(request):
    chu={}
    chu["timu"]=timuall(18)
    
    return render(request,"myen/testshowall.html",{"zd_list":chu})

def timuall(user_id):
    jieguo=[]
    mysql="select * from jilu where user_id={0}".format(user_id)
    timu30=sql_du(mysql)["shuju"]
    for i in timu30:
        jieguo.append(timu_dan(i[0],i[2]))
    # jieguo.append(timu30)
    print(jieguo)
    return jieguo

def timu_dan(myid,timu_id):
    #返回list
    jieguo=[]
    mysql="select * from lishi where myid={0}".format(timu_id)
    tm=sql_du(mysql)["shuju"][0]
    tm_ls=tm[2].split("^")
    # print(tm[2])
    # jieguo.append(tm_ls)
    jieguo.append(tm_ls[0]+"<ol type=A>")
    a=""
    for i in range(1,len(tm_ls)-1):
        if tm_ls[-1]==chr(i+64):
            a=a+"<li><input type=radio value={0}ok name={1}>{2}</li>".format(chr(64+i),myid,tm_ls[i])
        else:
            a=a+"<li><input type=radio value={0} name={1}>{2}</li>".format(chr(64+i),myid,tm_ls[i])
            
    
    a=a+"</ol>"
    jieguo.append(a)
    
    return jieguo

def timujieguo(request):
    jieguo=[]
    daan=[]
    mysql="select * from jilu where user_id={0}".format(18)
    hui=sql_du(mysql)["shuju"]
    jian="R2"
    banji=request.POST
    print((banji))

    
    # chu=banji["R1"]
    defen=0
    for m,n in banji.items() :
        
        if len(n)==3 :
            defen=defen+1
            mysql="update jilu set daan='{0}' , defen={1} where myid={2}".format(n[0],1,m)
        if len(n)==1:
            mysql="update jilu set daan='{0}' , defen={1} where myid={2}".format(n,0,m)
        # print(m,n)
        print(mysql)
        a=sql_xie(mysql)
    chu="总计得分：{0}".format(defen)
    
    
    
    return render(request,"myen/myshow.html",{"zd_list":chu})

    
    
    


