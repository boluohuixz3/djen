from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader,RequestContext
import time
print(time.asctime())


# Create your views here.
def index(request):
    import os 
    zd=[]
    a=['汉语翻译',"myen/cs_danci/"]
    zd.append(['单词翻译',"myen/cs_fanyi_2/?ok_id=0&danci_id=0"] )
    zd.append(a )
    print(zd)
    return render(request, 'all.html',  {"zd_list":zd})

# def guanli(request):

#     return render(request, 'myen/sqlindex.htm')