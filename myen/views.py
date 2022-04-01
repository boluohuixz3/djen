from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader,RequestContext
import time
print(time.asctime())


# Create your views here.
def allindex(request):
    import os 
    ml=os.getcwd()+"\\myen\\urls.py"
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
    
    return render(request, 'myen/all.html',  {"zd_list":zd})

# def guanli(request):

#     return render(request, 'myen/sqlindex.htm')