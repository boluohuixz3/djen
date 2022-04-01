from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader,RequestContext
from django.shortcuts import render
from django.views.decorators import csrf
import random
import time
import os
import sqlite3
# Create your views here.
print("tou",time.time())
def tou_show(jibie):
    sj='''
<table border="1" width="100%" id="table1">
	<tr>
		<td align="center"><a href=/myen/sql1/>数据库</a></td>
		<td align="center"><a href=/myen/sqlcreate/ >建表</a></td>
		<td align="center"><a href=/myen/zj_xueke/>分类管理</a></td>
		<td align="center">查看</td>
		<td align="center">删除</td>
		<td align="center">题目添加</td>
		<td align="center">上传</td>
	</tr>
</table>
<table border="1" width="100%" id="table1">
	<tr>
		<td align="center"><a href=/myen/sql1/>数据库</a></td>
		<td align="center">建表</td>
		<td align="center"><a href=/myen/zj_xueke/>分类管理</a></td>
		<td align="center">查看</td>
		<td align="center">删除</td>
		<td align="center">题目添加</td>
		<td align="center">上传</td>
	</tr>
</table>

'''
    return sj

def getml(wen):
    myml=os.getcwd()+"\\"+wen
    return(myml)

print(getml("en.sqlite3"))
def sqlguanli(request):
    #功能：显示所有表名，链接显示内容
    ml=getml("en.sqlite3")
    #print(ml)
#    ml=ml.replace("\\",r"\\")
    conn=sqlite3.connect(ml)
    sj = conn.cursor()
    
    jg=[]
    zd={}

    sj.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    zd1=sj.fetchall()
    chuli=[]
    
    for i in zd1:
        jg.append(i[0])
            
#    print(jg)
    zd["shuju"]=jg
    zd['ku']=ml
    sj.close
    conn.close

    return render(request, 'myen/sqlindex.htm',{"zd_list":zd})

def sql_list(request):
    zd={}
    zz1=request.GET.get('question_id','')

    zz2=request.GET.get('page_id')
    
    ye=int(zz2)
    xian=" "+str((ye-1)*100)+",100"
    ye1=ye-1
    if ye1<=1:
        ye1=1
    zd['biao']=zz1
    zd['ye1']=ye1
    zd['ye2']=ye+1
    zd['ye']=ye
    
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    
    jg=[]
    

    sj.execute("SELECT * FROM "+ zz1 +"  limit  " +xian )
    zd1=sj.fetchall()
    des = sj.description
    zd["tou"]=des
 

    zd["shuju"]=zd1
    sj.close 
    conn.close
    
    return render(request, 'myen/sql_list.htm',  {"zd_list":zd})

def sql_listall(request):
    zd={}
    zz1=request.GET.get('question_id','')

    zz2=request.GET.get('page_id')
    
    ye=int(zz2)
    xian=" "+str((ye-1)*100)+",100"
    ye1=ye-1
    if ye1<=1:
        ye1=1
    zd['biao']=zz1
    zd['ye1']=ye1
    zd['ye2']=ye+1
    zd['ye']=ye
    
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    
    jg=[]
    

    sj.execute("SELECT * FROM "+ zz1  )
    zd1=sj.fetchall()
    des = sj.description
    zd["tou"]=des
    for i in des:
        print(i[0])
   

    chuli=[]

    zd["shuju"]=zd1
    sj.close 
    conn.close
    
    return render(request, 'myen/sql_list.htm',  {"zd_list":zd})

def sql_create(request):

    return render(request, 'myen/sql_create.htm')


def sql_list2(request):
    zd={}
    zz1=request.GET.get('question_id','')
    zz2=request.GET.get('page_id')
    ye=int(zz2)+1
    zd['biao']=zz1
    zd['ye']=ye
       
    return render(request, 'myen/sql_list.htm',  {"zd_list":zd})

def sql_create(request):

    return render(request, 'myen/sql_create.htm')

def sql_create1(request):
    ctx ={}
    mysql=""
    if request.POST:
        zd=[]
        if len(request.POST['T2'])>=2 :
            mysql=mysql+(request.POST['T2'])+"  NONE,"
        if len(request.POST['T3'])>=2 :
            mysql=mysql+(request.POST['T3'])+"  NONE,"
        if len(request.POST['T4'])>=2 :
            mysql=mysql+(request.POST['T4'])+"  NONE,"
        if len(request.POST['T5'])>=2 :
            mysql=mysql+(request.POST['T5'])+"  NONE,"
        if len(request.POST['T6'])>=2 :
            mysql=mysql+(request.POST['T6'])+"  NONE,"
        
    mysql=mysql[0:len(mysql)-1]
    mysql=mysql="CREATE TABLE "+request.POST['T1']+" (myid  INTEGER PRIMARY KEY,"+mysql+")"
    ctx["jg"]=mysql
    ctx['biao']=request.POST['T1']
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    print(mysql)
    sj.execute(mysql)

    return render(request, "myen/sql_create1.html", {"zd_list":ctx})

def sql_shanbiao(request,question_id):
    zd={}
    zd['biao']=question_id+"删除成功"
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute("DELETE FROM  "+question_id)
    conn.commit()
    sj.execute("DROP TABLE "+question_id)
    conn.commit()
    conn.close
    
    return render(request, 'myen/sql_shanbiao.html',  {"zd_list":zd})

def sql_shujuadd(request,question_id):
    zd={}
    zd["biao"]=question_id
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute("SELECT * FROM "+ question_id +"  limit 2")
    des = sj.description
    zd["tou"]=des


    return render(request, 'myen/sql_shujuadd.html',{"zd_list":zd})


def sql_shujuadd2(request,question_id):
    fx=request.POST.getlist("CC")
    zd={}
    zd["biao"]=question_id
    cc= request.POST['S1']
    aa=cc.replace(',',' ')
    aa=aa.replace('\r\n','^')
    aa=aa.replace('\t',',')
    if aa[-1]=="^":
        aa=aa[0:-1]
    dd=aa.split('^')
    gg=[]
    jieguo=[]
    for i in dd:
        gg=i.split(',')
        jieguo.append(gg)
    zd['shuju'] =jieguo
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    lie= ','.join(fx)
    js=0

    for i in jieguo:
        js=js+1
        zhi=""
        for b in i:
            zhi=zhi+"'"+b+"',"
        zhi=zhi[0:len(zhi)-1]
        mysql="insert into "+question_id+"("+lie+") values("+zhi+")"
        print("数据：",mysql)
        sj.execute("insert into "+question_id+"("+lie+") values("+zhi+")")
                
    conn.commit()

    zd['zong']=js



    return render(request, 'myen/sql_shujuadd2.html',{"zd_list":zd})


def sql_ziduanadd(request,question_id):
    zd={}
    zd["biao"]=question_id

    return render(request, 'myen/sql_ziduanadd.htm',{"zd_list":zd})

def sql_ziduanadd2(request,question_id):
    ctx ={}
    mysql=""
    # if request.POST:
    #     if len(request.POST['T1'])>=2 :
    mysql="ALTER TABLE "+question_id+" add "+request.POST['T1']+"  "+request.POST['D1']
       
        
   
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute(mysql)
    conn.commit()
    ctx['jg']=mysql
    ctx['biao']=mysql

    return render(request, "myen/sql_ziduanadd2.htm", {"zd_list":ctx})


def sql_ml(request):
   

    return render(request, 'myen/sql_ml.htm')

def sql_ml2(request):
    ctx ={}
    mysql=""
    # if request.POST:
    #     if len(request.POST['T1'])>=2 :
    mysql=request.POST['T1']
       
        
   
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute(mysql)
    conn.commit()
    ctx['jg']=mysql
   

    return render(request, "myen/sql_ziduanadd2.htm", {"zd_list":ctx})



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
def list_del(mysql):
    #通用sql语句，无返回值
    zd={}
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    sj.execute(mysql)
    conn.commit()

    sj.close 
    conn.close
    
    return zd


def list_add(mysql):
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    print(mysql)
    sj.execute(mysql)
    conn.commit()
    sj.close 
    conn.close
    
    return "ok"


def zj_xueke(request):
    zd={}
    zd=list_all("select * from zhangjie where xiangmu='学科' ")
    jg=zd['shuju']
    maxshu=len(jg)
    if maxshu<1:
        shu=10000000
    else:
        shu=jg[maxshu-1][3]+1000000
    if request.POST:
        if len(request.POST['T1'])>=2 :
            a=list_add("insert into zhangjie(xiangmu,mingcheng,daima) values('学科','"+request.POST['T1']+"','"+str(shu)+"')")
            zd=list_all("select * from zhangjie where xiangmu='学科' ")  #再次刷新页面
    zd["caidan"]=tou_show(1)
   
    return render(request, 'myen/zj_xueke.htm',  {"zd_list":zd})


def sql_del(request):
    zd={}
    zz1=request.GET.get('bm_id','')
    zz2=request.GET.get('sj_id')
    mysql="delete from "+zz1 +" where myid="+zz2
    print(mysql)
    a=list_del(mysql)
    zd['shuju']=mysql



    
    return render(request, 'myen/sql_dell.htm',  {"zd_list":zd})

def sql_dellall(request):
    #删除全部数据
    zd={}
    zz1=request.GET.get('bm_id','')
    mysql="delete from "+zz1
    a=list_del(mysql)
    zd['shuju']=mysql

    
    
    return render(request, 'myen/sql_dellall.htm',   {"zd_list":zd})


def zj_nianji(request):
    zd={}
    jg=[]
    xk=request.GET.get('xk')
    dm=request.GET.get('dm')
    zd['xk']=xk
    zd['dm']=dm
    mysql="select * from zhangjie where xiangmu='年级' and daima >="+dm + " and daima <="+str(eval(dm)+999999)
    sj=list_all(mysql)
    zd['shuju']=sj['shuju']
    maxshu=len(sj['shuju'])
    jg=sj['shuju']
   
    if request.POST:
        if maxshu<1:
            shu=eval(dm)+100000
        else:
            shu=jg[maxshu-1][3]+10000
        if len(request.POST['T1'])>=1 :
            a=list_add("insert into zhangjie(xiangmu,mingcheng,daima) values('年级','"+request.POST['T1']+"','"+str(shu)+"')")
            sj=list_all(mysql)  #再次刷新页面
    zd['caidan']=tou_show(1)
    zd['shuju']=sj['shuju']
    zd['tou']=sj['tou']

   
    return render(request, 'myen/zj_nianji.htm',  {"zd_list":zd})


def zj_nianjiduo(request):
    zd={}
    jg=[]
    xk=request.GET.get('xk')
    dm=request.GET.get('dm')
    zd['xk']=xk
    zd['dm']=dm
    mysql="select * from zhangjie where xiangmu='年级' and daima >="+dm + " and daima <="+str(eval(dm)+999999)
    sj=list_all(mysql)
    zd['shuju']=sj['shuju']
    maxshu=len(sj['shuju'])
    jg=sj['shuju']
   
    # if request.POST:
    #     if maxshu<1:
    #         shu=eval(dm)+100000
    #     else:
    #         shu=jg[maxshu-1][3]+10000
    #     if len(request.POST['T1'])>=1 :
    #         a=list_add("insert into zhangjie(xiangmu,mingcheng,daima) values('年级','"+request.POST['T1']+"','"+str(shu)+"')")
    #         sj=list_all(mysql)  #再次刷新页面
    # zd['caidan']=tou_show(1)
    # zd['shuju']=sj['shuju']
    # zd['tou']=sj['tou']

   
    return render(request, 'myen/zj_nianji.htm',  {"zd_list":zd})


def zj_zhang(request):
    zd={}
    jg=[]
    xk=request.GET.get('xk')
    dm=request.GET.get('dm')
    zd['xk']=xk
    zd['dm']=dm
    print(xk,dm)
    mysql="select * from zhangjie where xiangmu='章节' and daima >="+dm + " and daima <="+str(eval(dm)+9999)
    print(mysql)
    sj=list_all(mysql)
    zd['shuju']=sj['shuju']
    maxshu=len(sj['shuju'])
    jg=sj['shuju']
   
    if request.POST:
        if maxshu<1:
            shu=eval(dm)+1000
        else:
            shu=jg[maxshu-1][3]+100
        if len(request.POST['S1'])>=1 :
            js=request.POST['S1']
            print(js)
            js=js.replace('\r\n','^')
            print(js)
            if js[-1]=='^':
                js=js[0:-1]
            js_ls=js.split('^')
            print(js_ls)
            jiafa=0
            for i in js_ls:
                a=list_add("insert into zhangjie(xiangmu,mingcheng,daima) values('章节','"+i+"','"+str(shu+jiafa)+"')")
                jiafa=jiafa+100
            sj=list_all(mysql)  #再次刷新页面
    zd['caidan']=tou_show(1)
    zd['shuju']=sj['shuju']
    zd['tou']=sj['tou']

   
    return render(request, 'myen/zj_zhang.htm',  {"zd_list":zd})


def zj_xueke_duo(request):
    zd={}
    mysql="select * from zhangjie where xiangmu='学科' "
    fhsql=list_all(mysql)
    jg=fhsql['shuju']
    zd['shuju']=fhsql['shuju']
    zd['tou']=fhsql['tou']

    maxshu=len(jg)
    if request.POST:
        if maxshu<1:
            jiafa=10000000
        else:
            jiafa=jg[maxshu-1][3]+1000000
        if len(request.POST['S1'])>=1 :
            js=request.POST['S1']
            print(js)
            js=js.replace('\r\n','^')
            if js[-1]=='^':
                js=js[0:-1]
            js_ls=js.split('^')
            print(js_ls)
            for i in js_ls:
                a=list_add("insert into zhangjie(xiangmu,mingcheng,daima) values('学科','"+i+"','"+str(jiafa)+"')")
                jiafa=jiafa+1000000
            sj=list_all(mysql)  #再次刷新页面
            zd['shuju']=sj['shuju']
            zd['tou']=sj['tou']

    zd['caidan']=tou_show(1)
  
    return render(request, 'myen/zj_xueke.htm',  {"zd_list":zd})

def nianji_duo(request):
    zd={}
    jg=[]
    xk=request.GET.get('xk')
    dm=request.GET.get('dm')
    zd['xk']=xk
    zd['dm']=dm
    mysql="select * from zhangjie where xiangmu='年级' and daima >="+dm + " and daima <="+str(eval(dm)+999999)
    sj=list_all(mysql)
    zd['shuju']=sj['shuju']
    jg=sj['shuju']
    maxshu=len(jg)
    print(mysql)
    if request.POST:
               
        if len(request.POST['S1'])>=1 :
            js=request.POST['S1']
            print(js,xk,dm)
            js=js.replace('\r\n','^')
            if js[-1]=='^':
                js=js[0:-1]
            js_ls=js.split('^')
        if maxshu<1:
            jiafa=eval(dm)+100000
        else:
            jiafa=jg[maxshu-1][3]+10000

        for i in js_ls:
            a=list_add("insert into zhangjie(xiangmu,mingcheng,daima) values('年级','"+i+"','"+str(jiafa)+"')")
            jiafa=jiafa+10000
    
    sj=list_all(mysql)  #再次刷新页面
    
    
    
    zd['caidan']=tou_show(1)
    zd['shuju']=sj['shuju']
    zd['tou']=sj['tou']

   
    return render(request, 'myen/zj_nianji.htm',  {"zd_list":zd})

def tm_add1(request):
    zd={}
    zd["shuju"]=time.time()
    return render(request, 'myen/tm_add.html',{'zd_list':zd})



def tm_add2(request):
    timu1=[]
    timu2=[]
    zd={}
    if request.POST:
        shuru=request.POST['S1']
        xueke=request.POST['D1']
        if len(request.POST['S1'])>=1 :
            shuru=shuru.replace('\r\n','^')
            if shuru[-1]=='^':
                shuru=shuru[0:-1]
            js_ls=shuru.split('^')
            bianhao=0
            for i in js_ls:
                if len(i)>0:
                    timu2.append(i)
                else:
                    timu1.append(timu2)
                    timu2=[]
            timu1.append(timu2)
            for i in timu1:
                print(i[0])
                tigan=i[0]
                daan=i[-1].upper()
                xuanxiang=""
                zm=65
                for a in range(1,len(i)-1):
                    xuanxiang=xuanxiang+"<input type=radio   name=R1 value="+chr(zm)+">" +chr(zm)+" "+i[a]+"<br><br>"
                    zm=zm+1
                
               # mysql="insert into timu(leibie,zhengwen,lishu,beizhu) values('选择','"+tigan+"','"+xuanxiang+"','"+daan+"')"
                mysql="insert into timu(leibie,zhengwen,lishu,beizhu,chuti,cuowu,zhangjie) values('选择','"+tigan+"','"+xuanxiang+"','"+daan+"',100,0,'"+xueke+"')"
       
                
                a=list_del(mysql)


 
            zd['shuju']=mysql


    return render(request, 'myen/tm_add2.html',{'zd_list':zd})


def tm_list1(request):
    zd={}

    mysql="select * from timu "
    sj=list_all(mysql)


    zd['caidan']=tou_show(1)
    zd['shuju']=sj['shuju']
    print(sj['shuju'])
    zd['tou']=sj['tou']
    return render(request, 'myen/tm_list.html',  {"zd_list":zd})

def tm_add_dx1(request):
    zd={}
    zd["shuju"]=time.time()
    return render(request, 'myen/tm_add_dx.html',{'zd_list':zd})


def tm_add_dx2(request):
    timu1=[]
    timu2=[]
    zd={}
    if request.POST:
        xueke=request.POST['D1']
        shuru=request.POST['S1']
        if len(request.POST['S1'])>=1 :
            shuru=shuru.replace('\r\n','^')
            if shuru[-1]=='^':
                shuru=shuru[0:-1]
            js_ls=shuru.split('^')
            bianhao=0
            for i in js_ls:
                if len(i)>0:
                    timu2.append(i)
                else:
                    timu1.append(timu2)
                    timu2=[]
            timu1.append(timu2)
            for i in timu1:
                
                tigan=i[0]
                daan=i[-1].upper()
                xuanxiang=""
                zm=65
                for a in range(1,len(i)-1):
                    xuanxiang=xuanxiang+"<input type=checkbox name=R1 value="+chr(zm)+">" +chr(zm)+" "+i[a]+"<br><br>"
                    zm=zm+1
                
             #   mysql="insert into timu(leibie,zhengwen,lishu,beizhu) values('选择','"+tigan+"','"+xuanxiang+"','"+daan+"')"
                mysql="insert into timu(leibie,zhengwen,lishu,beizhu,chuti,cuowu,xueke) values('选择','"+tigan+"','"+xuanxiang+"','"+daan+"',100,0,'"+xueke+"')"
       
                a=list_del(mysql)

            zd['shuju']=mysql
    return render(request, 'myen/tm_add_dx2.html',{'zd_list':zd})

def tm_add_tk1(request):
    zd={}
    zd["shuju"]=time.time()
    return render(request, 'myen/tm_add_tk.html',{'zd_list':zd})

def tm_add_tk2(request):
    timu1=[]
    timu2=[]
    zd={}
    if request.POST:
        shuru=request.POST['S1']
        xueke=request.POST['D1']
        if len(request.POST['S1'])>=1 :
            shuru=shuru.replace('\r\n','^')
            shuru=shuru.replace('^^^','^')
            shuru=shuru.replace('^^','^')
            
            print("shuru:",shuru)
            if shuru[-1]=='^':
                shuru=shuru[0:-1]
            js_ls=shuru.split('^')
            # print(js_ls)
            bianhao=0
            # for i in js_ls:
            #     if len(i)>0:
            #         timu2.append(i)
            #     else:
            #         timu1.append(timu2)
            #         timu2=[]
            # timu1.append(timu2)
            he=len(js_ls)
            addjg=""
            print(he)
            if he % 2==0:
                for i  in range(0,he,2):
                    
                    tigan=str(js_ls[i])

                    daan=str(js_ls[i+1])
                    xuanxiang="空"
                    mysql="insert into timu(leibie,zhengwen,lishu,beizhu,zhangjie) values('填空','"+tigan+"','"+xuanxiang+"','"+daan+"','"+xueke+"')"
                    print(mysql)
                    a=list_del(mysql)
                    addjg=addjg+tigan[0:10]+"......添加成功<br>"
            else:
                addjg="内容错误，题目和答案不匹配"
                
            zd['shuju']=addjg

            
    return render(request, 'myen/tm_add_tk2.html',{'zd_list':zd})

def tk(wen):
    tkwen=wen.replace("_ ","<input type=text name=T1 size=1> ")
    print(tkwen)
    return tkwen

def tm_add_tu1(request):
    zd={}
    zd["shuju"]=time.time()
    return render(request, 'myen/tm_add_tu1.html',{'zd_list':zd})


def tm_add_tu2(request):
    zd={}
    zd["shuju"]=time.time()
     #多文件上传
    import os
    # ml=os.getcwd()+"\\polls\\templates\\"
    ml=os.getcwd()+"\\static\\myen\\images\\" #上传目录
    obj = request.FILES.getlist('F1',None)
  #  print(ml)
    ctx={}
    shuru=request.POST['S1']
    xueke=request.POST['D1']
    daan_l=[]
    daan_l=shuru.split(',')
    tigan=""
    xuanxiang=""
    daan=""
    
    wen_name=""
    i=0
    for fi in obj:
        wen_name=wen_name+"<br>"+fi.name
           
        new_wen=str(int(time.time()*1000)*10000+random.randrange(100,999))+fi.name[-4:]

        
        f = open(os.path.join(ml, new_wen), 'wb')
        for chunk in fi.chunks():
            f.write(chunk)
        f.close()
        tigan="/myen/images/"+new_wen
        daan=daan_l[i]
        if  len(daan_l[i])==1:
            xuanxiang="<p>A<input type=radio value=A name=R1>&nbsp; B<input type=radio value=B name=R1>&nbsp; 	C<input type=radio value=C name=R1>&nbsp; D<input type=radio value=D name=R1>&nbsp; E<input type=radio value=E name=R1>"
        else:
            xuanxiang="A<input type=checkbox name=R1 value=A>&nbsp; B<input type=checkbox name=R1 value=B>&nbsp; C<input type=checkbox name=R1 value=C>&nbsp; D<input type=checkbox name=R1 value=D>&nbsp; E<input type=checkbox name=R1 value=E>&nbsp;"
        mysql="insert into timu(leibie,zhengwen,lishu,beizhu,chuti,cuowu,xueke) values('选择','"+tigan+"','"+xuanxiang+"','"+daan+"',100,0,'"+xueke+"')"
       
      #  print(mysql)
        list_del(mysql)
        i=i+1
    ctx["xian"]=wen_name+"<br>成功"
    return render(request, 'myen/tm_add_tu2.html',{'zd_list':ctx})


def sql_xiugai(request,question_id):
    #修改前全部显示页面
    zd={}
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    mysql="SELECT * FROM "+question_id
    zd['biao']=question_id
    sj.execute(mysql)
 #   conn.commit()
    zd1=sj.fetchall()
    des = sj.description
    zd["tou"]=des
   
    zd["shuju"]=zd1
    sj.close 
    conn.close
    return render(request, 'myen/sql_xiugai1.html',{'zd_list':zd})


def sql_xiugai1(request):
    #修改前全部显示页面
    zz1=request.GET.get('bm_id','')
    zz2=request.GET.get('sj_id','')

    print(zz1)
    print(zz2)
    zd={}
    zd['sj_id']=zz2
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    mysql="SELECT * FROM "+zz1+" where myid="+zz2
    print(mysql)
    zd['biao']=zz1
    sj.execute(mysql)
 #   conn.commit()
    zd1=sj.fetchall()
    des = sj.description
    zd["tou"]=des
   
    zd["shuju"]=zd1
    sj.close 
    conn.close
    return render(request, 'myen/sql_xiugai2.html',{'zd_list':zd})

def sql_xiugai2(request):
    #修改数据写入数据库
    zz3=[]
    zz1=request.GET.get('bm_id','')
    zz2=request.GET.get('sj_id','')

    fx=[]
    fx=request.POST.getlist("TT")   #必须用字符，不能用数字，文本框名称

    zd={}
    zd['cs']='ok'
    zd['biao']=zz1
    zd['sj_id']=zz2
    zd['neirong']=fx
    
    ml=getml("en.sqlite3")
    conn=sqlite3.connect(ml) #创建指定数据库 硬盘
    sj = conn.cursor()
    mysql="SELECT * FROM "+zz1+" where myid="+zz2
    
#     zd['biao']=zz1
    sj.execute(mysql)
    conn.commit()
    zd1=sj.fetchall()
    des = sj.description
    sj.close()

   

    tou=[]
    for i in des:
        tou.append(i[0])
    tou.pop(0)
    fx.pop(0)
    dictionary = dict(zip(tou,fx))
    cs=""
    for x,y in dictionary.items():
        print(x,"=",y)
        cs=cs+", "+ x +"='"+y+"' "
    
    cs=cs[1:]
    mysql="update "+zz1+" set "+cs+" where myid="+zz2
    
    sj2 = conn.cursor()
    sj2.execute(mysql)
    conn.commit()




    
#     zd1=sj.fetchall()
#     des = sj.description
#     zd["tou"]=des
   
#     zd["shuju"]=zd1
#     sj.close 
#     conn.close
    return render(request, 'myen/sql_xiugai3.html',{'zd_list':zd})