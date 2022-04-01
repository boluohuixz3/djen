from django.shortcuts import render
from django.views.decorators import csrf
 
# 接收POST请求数据
def search_post(request):
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





    return render(request, "polls/post.html", ctx)