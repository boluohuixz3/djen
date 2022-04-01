from django.urls import path
from django.conf.urls import url
from . import myviews
from . import views,search2,search
from . import mypost
app_name = 'polls'
urlpatterns = [
    path('index/', views.index, name='index'),
     # ex: /polls/
 #   path('/', views.allindex, name='allindex'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('runoob/', views.runoob, name='runoob'),
    path('runoobtime/', myviews.runoobtime, name='runoobtime'),
    path('runoobzd/', myviews.runoobzd, name='runoobzd'),
    path('runooblist/', myviews.runooblist, name='runooblist'),
    path('runooblist2/', myviews.runooblist2, name='runooblist2'),
    path('runoobzd2/', myviews.runoobzd2, name='runoobzd2'),
    path('runoobdata/', myviews.runoobdata, name='runoobdata'),
    path('runoobdata2/', myviews.runoobdata, name='runoobdata2'),
    path('tabledata/', myviews.tabledata, name='tabledata'),
    path('tableday/', myviews.tableday, name='tableday'),
    path('tablecode/', myviews.tablecode, name='tablecode'),
    path('tableday/<str:question_id>/', myviews.daylist, name='daylist'),
    path('tablecode/<str:question_id>/', myviews.codelist, name='codelist'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^search-post/$', search2.search_post),
    path('postall/', mypost.post_form, name='post_form'),
    path('post_data/', mypost.post_data, name='post_data'),
    path('postwen/', mypost.post_wen, name="postwen1"),
    path('postwen2/', mypost.post_wen2, name="postwen2"),
    path('1posttext/', mypost.post_text, name='post_text'),
    path('1posttext2/', mypost.post_text2, name='post_text2'),
    
    

    
]