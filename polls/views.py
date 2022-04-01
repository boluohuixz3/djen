from django.http import HttpResponse
from django.http import Http404
from django.template import loader,RequestContext
from django.shortcuts import get_object_or_404, render
from .models import Question,Choice
from django.shortcuts import render
from django.urls import reverse
from django.views import generic



def index(request):
    
    context = {'latest_question_list': "latest_question_list"}
    return render(request, 'polls/index2.html', context)

def allindex(request):
    import os 
    ml=os.getcwd()+"\\polls\\urls.py"
    ml=ml.replace("\\",r"\\")
    wen=[]
    fn =open(ml,"rt")
    a=fn.readline()
    ss=""
    zd =[]
    url1=[]
    while True:
        c=[]
        url1=[]
        if not a:
            break
        a=fn.readline()
        if (a.find("path(")>-1) :
             c=a.split(",")
             ss=c[0]
             ss=ss[10:len(ss)-1]
             url1.append(ss)
             ss=c[1]
             url1.append(ss)
             ss=c[2]
             ss=ss[7:len(ss)-2]
             url1.append(ss)
             zd.append(url1)
        c=[]
        ss=""
        if (a.find("url(")>-1) :
             c=a.split(",")
             ss=c[0]
             ss=ss[11:len(ss)-2]
             url1.append(ss)

             ss=c[1]
             ss=ss[0:len(ss)-1]
            
             url1.append(ss)
             url1.append("无")
             zd.append(url1)
    fn.close
    url1.append("001")
    url1.append("ceshi")
    
    return render(request, 'polls/all.html',  {"zd_list":zd})



def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def runoob(request):
    context          = {}
    
    context['hello'] = 'Hello World!'
    return render(request, 'polls/runoob.html', context)


# 表单
def search_form(request):
    return render(request, 'polls/search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    # if 'q' in request.GET['q'] and request.GET['q']:
    #     message = '你搜索的内容为: ' + request.GET['q']
    # else:
    #     message = '你提交了空表单shide'
    message=request.GET['q']
    return HttpResponse(message)

def login_2(request):
    form_obg = forms.login_form(); #//必须先实例化表单
    if request.method=="POST":
        form_obg = forms.login_form(request.POST);   #---->将前端提交上来的字段加入表单
        if form_obg.is_valid():  #---------------->通过表单中定义的规则对表单的所有数据进行检查，如果检查通过，说明验证通过
            return HttpResponse("登陆成功");
    return render(request,"login2.html",{'form_obj':form_obg});#---------->最终都要返回表单字段