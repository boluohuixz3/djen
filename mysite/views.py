from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader,RequestContext
import time
print(time.asctime())


# Create your views here.
def index(request):
    import os 
    zd=[
        ['汉语翻译',"/myen/cs_danci/"],
        ['单词翻译',"/myen/cs_fanyi_2/?ok_id=0&danci_id=0"],
        ['填空语文',"/myen/chuti_tk/?xueke=语文"],
        ['填空历史',"/myen/chuti_tk/?xueke=历史"]
    ]
    

    print(zd)
    return render(request, 'all.html',  {"zd_list":zd})

def index0(request):
    zd=[]
   
    return render(request, 'all2.html')

# def guanli(request):

#     return render(request, 'myen/sqlindex.htm')