from django.shortcuts import render
from django.views.decorators import csrf
 
# 接收POST请求数据

def post_form(request):
    return render(request, 'polls/postall.html')

def post_data(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
        ctx['rlt1'] = request.POST['q2']
        ctx['rlt2'] = request.POST['q3']
        ctx['rlt3'] = request.POST['R1']
        fx=[]
        fx=request.POST.getlist("CC")
        ctx['rlt4']=fx


        ctx['D1'] = request.POST['D1']
    return render(request, "polls/postlist.html", ctx)

def post_wen(request):
    return render(request, 'polls/post_wen.html')

def post_wen2(request):
    #多文件上传
    import os
   # ml=os.getcwd()+"\\polls\\templates\\"
    ml=os.getcwd()+"\\templates\\polls\image\\" #上传目录
    obj = request.FILES.getlist('F1',None)
    
    ctx={}
    ctx["xian"]=obj
    for fi in obj:
        print(fi.name)
        f = open(os.path.join(ml, fi.name), 'wb')
        for chunk in fi.chunks():
            f.write(chunk)
        f.close()



    #ctx["wenname"]=obj.name
    # cc=obj.name
    # ctx["wentype"]=cc
    # f = open(os.path.join(ml, obj.name), 'wb')
    # for chunk in obj.chunks():
    #     f.write(chunk)
    # f.close()
    # # # ctx["wenname"]=obj.name
    # ctx['mulu']=ml
    return render(request, "polls/post_wen2.html", {"shuchu":ctx})

def post_text(request):
    return render(request, 'polls/post_text.html')

def post_text2(request):
    ctx={}
    cc= request.POST['S1']
    aa=cc.replace(',','')
    aa=aa.replace('\r\n','!')
    aa=aa.replace('\t',',')
    dd=aa.split('!')
    gg=[]
    jieguo=[]
    for i in dd:
        print(i)
        gg=i.split(',')
        print("gg",gg)
        jieguo.append(gg)

    
    
     #   a=sp
    print(jieguo)
    ctx['shuju'] = jieguo
    ctx['mulu']="ml"
    return render(request, "polls/post_text2.html", {"shuchu":ctx})

def djcs(request):
    zd=[1,2,3,4,5,8,4,"a","c","d"]
    return render(request, 'polls/myshow.html',{"zd_list":zd})