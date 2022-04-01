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

  
def tou_show(jibie):
    sj='''
<table border="1" width="100%" id="table1">
	<tr>
		<td align="center">学科章节</td>
		<td align="center">添加题目</td>
		<td align="center">题目查看</td>
		<td align="center">查看</td>
		<td align="center">删除</td>
		<td align="center">添加</td>
		<td align="center">上传</td>
	</tr>
</table>

'''
    return sj  

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

def cs_suiji(request):
    ctx ={}
    mysql="select * from danci  order  by  newid()"

    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute("select * from danci ORDER BY RANDOM() limit 20")
    ctx['jg']=mysql
    zd1=sj.fetchall()
    des = sj.description
    ctx["tou"]=des
    ctx["shuju"]=zd1
    sj.close 
    conn.close
   

    return render(request, "myen/cs_list.htm", {"zd_list":ctx})

def cs_fanyi(request):
    from random import randint
    yuan1=request.session.get("old_danci")
    yuan2=request.session.get("old_hanyu")
    yuan3=request.session.get("danci_id")

    ctx ={}
    zd1=[]
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute("select * from danci  ORDER BY chuti, RANDOM()  limit 10")
    zd1=sj.fetchall()
   
    i=randint(0,len(zd1)-1)
    #print("总数，喧杂",len(zd1),i)

    ctx['danci']=zd1[i][1]
    ctx['cixing']=zd1[i][4]
    ctx['jieguo']=zd1[i][3]
    ctx['old1']=yuan1
    ctx['old2']=yuan2
    request.session["old_danci"]=zd1[i][1]
    request.session["old_hanyu"]=zd1[i][3]
    request.session["danci_id"]=zd1[i][0]
    ctx["hanyu"]=zd1
  
    if request.POST:
        if request.POST['R1'] in yuan2:
            mysql="update danci set chuti=chuti+1,cuowu=2 where myid=" + str(yuan3)
            ctx['xuanze'] = request.POST['R1'] +"    正确！"
            sj.execute(mysql)
            ctx['se']=' bgcolor="#00FF00" '

        else:
            mysql="update danci set chuti=chuti-4, cuowu=1 where  myid=" + str(yuan3)
            ctx['xuanze'] = request.POST['R1'] +"    错误！"
            sj.execute(mysql)
            ctx['se']=' bgcolor=#FF0000 '
        conn.commit()
    
    sj.execute("SELECT count(danci) FROM danci")
    zd1=sj.fetchall() 
    ctx['alldanci']=zd1
    
    sj.execute("SELECT count(danci) FROM danci where chuti >100")
    zd1=sj.fetchall() 
    ctx['alldanci_ok']=zd1

   

    return render(request, "myen/fanyi.html", {"zd_list":ctx})


def cs_fanyi2(request):
    from random import randint
    ctx ={}
    zd1=[]
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()

    zz2=request.GET.get('ok_id')#选择

    zz1=request.GET.get('danci_id') #单词

    if zz1>'0' and zz2>'0':
        sj.execute("select hanyu from danci  where myid=" +zz2)
        zd1=sj.fetchall()
        ctx["xuanze"]=zd1[0][0]

        sj.execute("select danci,hanyu from danci  where myid=" +zz1)
        zd1=sj.fetchall()
       
        ctx["old1"]=zd1[0][0]
        ctx["old2"]=zd1[0][1]
        

    
#随机生成单词
    
    sj.execute("select * from danci  ORDER BY chuti, RANDOM()  limit 10")
    zd1=sj.fetchall()
   
    i=randint(0,len(zd1)-1)
    #print("总数，喧杂",len(zd1),i)

    ctx['danci']=zd1[i][1]
    ctx['cixing']=zd1[i][4]
    ctx['jieguo']=zd1[i][3]
    ctx['danci_id']=zd1[i][0]

    # request.session["old_danci"]=zd1[i][1]
    # request.session["old_hanyu"]=zd1[i][3]
    # request.session["danci_id"]=zd1[i][0]
    ctx["hanyu"]=zd1
  
    if zz1>'0' and zz2>'0':



        if zz1==zz2:
            mysql="update danci set chuti=chuti+1,cuowu=2 where myid=" + zz1
            sj.execute(mysql)
            ctx['se']=' bgcolor="#00FF00" '

        else:
            mysql="update danci set chuti=chuti-4, cuowu=1 where  myid=" + zz1
            sj.execute(mysql)
            ctx['se']=' bgcolor=#FF0000 '
        conn.commit()
    #计数
    sj.execute("SELECT count(danci) FROM danci")
    zd1=sj.fetchall() 
    ctx['alldanci']=zd1
    
    sj.execute("SELECT count(danci) FROM danci where chuti >100")
    zd1=sj.fetchall() 
    ctx['alldanci_ok']=zd1

   

    return render(request, "myen/fanyi_2.html", {"zd_list":ctx})

def cs_danci(request):
    from random import randint
    zz1=request.GET.get('danci_id')

    ctx ={}
    zd1=[]
    zd2=[]


    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute("select * from danci where chuti >99 ORDER BY RANDOM()  limit 1")

    zd1=sj.fetchall()
    print(zd1)
    i=0
    ctx['danci']=zd1[i][1]
    ctx['cixing']=zd1[i][4]
    ctx['hanyu']=zd1[i][3]
    ctx['danci_id']=zd1[i][0]
    


    
    # print(ord(yuan2[-1]))


    if request.POST:
        sj.execute("select * from danci where myid="+zz1)

        zd2=sj.fetchall()

        yuan1=zd2[i][1]
        yuan2=zd2[i][3]
      
        yuan1.replace(' ','')
        yuan1.replace('　','')
        yuan1.replace('’','')
        yuan1.replace('‘','')
        ctx['old1']=yuan1
        ctx['old2']=yuan2
        cc="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        if yuan1[-1] not in cc:
            yuan1=yuan1[0:-1]
        


        shuru=request.POST['T1']
        shuru.replace(' ','')
        shuru.replace('　','')
        shuru.replace('’','')
        shuru.replace('‘','')
        shuru=shuru.lower()
        yuan1=yuan1.lower()

        if shuru == yuan1:
            
            mysql="update danci set chuti=chuti-1 where myid="+ zz1
            ctx['xuanze'] = request.POST['T1'] +"    正确！"
            sj.execute(mysql)
            ctx['se']=' bgcolor="#00FF00" '

        else:
            #print(shuru,yuan1)
            mysql="update danci set chuti=chuti+1 where  myid=" +zz1
            ctx['xuanze'] = request.POST['T1'] +"    错误！"
            sj.execute(mysql)
            ctx['se']=' bgcolor=#FF0000 '
        conn.commit()

        

    return render(request, "myen/danci.html", {"zd_list":ctx})

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

def chuti_dx1(request):
    zd1=[]
    xianshi={}
    
    zz2=request.GET.get('xueke')
    
    ctx=chuti('选择',zz2)
    
    
    xianshi['timu']=ctx
    xianshi['xueke']=zz2
   


    xianshi["tou"]=""
   
   
 

    return render(request, "myen/ct_dx1.html", {"zd_list":xianshi})


def chuti_dx2(request):
    xianshi={}
    if request.POST:
        ctx=request.POST.getlist("R1")
        zz2=request.GET.get('xueke')
        zz1=str(request.GET.get('tm_id'))
         
        
        xianshi['timu']=chuti_id(zz1)
        xianshi['xuanze']=ctx
        xianshi['xueke']=zz2
        
    xianshi["tou"]=""
    # xianshi["shuchu"]="".join(ctx)
    
   
   
   

    return render(request, "myen/ct_dx2.html", {"zd_list":xianshi})

def chuti_tk(request):
    zz2=str(request.GET.get('xueke'))
    timu=[]
    xianshi={}
    xianshi['leibie']="学习"
    timu=chuti('填空',zz2)
    xianshi['timu']=timu[0][3]
    xianshi['tm_id']=timu[0][0]
    xianshi['xueke']=timu[0][5]
    
      
   
   

    return render(request, "myen/ct_tk.html", {"zd_list":xianshi})

def chuti_tk1(request):
    zz2=str(request.GET.get('xueke'))
    zz1=str(request.GET.get('tm_id'))
    
    user_da= request.POST['T1'] 
    timu=[]
    xianshi={}
    xianshi['leibie']="学习"
    xianshi['xueke']=zz2
    xianshi['user_da']=user_da
    timu=chuti_id(zz1)
    xianshi['timu']=timu[0][3]
    xianshi['biao_da']=timu[0][4]
    xianshi['tm_id']=zz1
    mysql="update timu set chuti=chuti+1 where myid="+zz1
        # print(mysql)
    b=sql_db(mysql)
    # xianshi['xueke']=timu[0][5]

    return render(request, "myen/ct_tk1.html", {"zd_list":xianshi})

def chuti_tkbj(request):
    zz2=str(request.GET.get('caozuo'))
    zz3=request.GET.get('xueke')
    zz1=str(request.GET.get('id'))
    # print(len(zz1),zz1)
    if zz2[1:2]=='b':
        
        mysql="update timu set cuowu=cuowu+1 where myid="+zz1
        # print(mysql)
        b=sql_db(mysql)
        # return redirect('/myen/ct_tk1.html/?xueke=历史')
    
    if zz2[1:2]=='q':
        
        mysql="update timu set cuowu=cuowu-1 where myid="+zz1
        b=sql_db(mysql)
        # return redirect('/myen/ct_tk1.html/?xueke=历史')
    xianshi="ok"
        
       
        
    

    return redirect('/myen/chuti_tk/?xueke='+ zz3)

