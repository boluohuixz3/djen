from django.urls import path
from django.conf.urls import url
from . import mysql
from . import mycs,myls
from . import views
app_name = 'myen'
urlpatterns = [
    path('all/', views.allindex, name='allindex'),
    path('sql1/', mysql.sqlguanli, name='guanli'),
    url(r'^sqllist/$', mysql.sql_list, name='sql_list'),
    url(r'^sqllistall/$', mysql.sql_listall, name='sql_listall'),
    path('sqlcreate/', mysql.sql_create, name='sql_create'),
    path('sqlcreate1/', mysql.sql_create1, name='sql_create1'),
    path('sqlshanbiao/<str:question_id>/', mysql.sql_shanbiao, name='sql_shanbiao'),
    path('sqlshujuadd/<str:question_id>/', mysql.sql_shujuadd, name='sql_shujuadd'),
    path('sqlshujuadd2/<str:question_id>/', mysql.sql_shujuadd2, name='sql_shujuadd2'),
    path('ziduanadd/<str:question_id>/', mysql.sql_ziduanadd, name='sql_ziduanadd'),
    path('ziduanadd2/<str:question_id>/', mysql.sql_ziduanadd2, name='sql_ziduanadd2'),
    path('sqlml/', mysql.sql_ml, name='sql_ml'),
    path('sqlml2/', mysql.sql_ml2, name='sql_ml2'),
    path('cs_suiji/', mycs.cs_suiji, name='cs_suiji'),
    path('cs_fanyi/', mycs.cs_fanyi, name='cs_fanyi'),
    url(r'^cs_fanyi_2/$', mycs.cs_fanyi2, name='cs_fanyi2'),
    path('cs_danci/', mycs.cs_danci, name='cs_danci'),
    path('zj_xueke/', mysql.zj_xueke, name='zj_xueke'),
    url(r'^sql_dell/$', mysql.sql_del, name='sql_del'),
    url(r'^sql_dellall/$', mysql.sql_dellall, name='sql_dellall'),
    url(r'^duotianjia',mysql.nianji_duo),
    url(r'^zj_nianji/$', mysql.zj_nianji),
    url(r'^zj_zhang/$', mysql.zj_zhang),
    url(r'^duonianji/$', mysql.nianji_duo),
    path('zj_xuekeduo/', mysql.zj_xueke_duo, name='zj_xueke_duo'),
    path('tm_add/', mysql.tm_add1, name='tm_add1'),
    path('tm_add2/', mysql.tm_add2, name='tm_add2'),
    url(r'^tm_list/$', mysql.tm_list1),
    url(r'^tm_add_dx/$', mysql.tm_add_dx1),
    url(r'^tm_add_dx2/$', mysql.tm_add_dx2),
    url(r'^tm_add_tk/$', mysql.tm_add_tk1),
    url(r'^tm_add_tk2/$', mysql.tm_add_tk2),
    url(r'^ct_dx1/$', mycs.chuti_dx1),
    url(r'^ct_dx2/$', mycs.chuti_dx2),
    url(r'^tmaddtu1/$', mysql.tm_add_tu1),
    url(r'^tmaddtu2/$', mysql.tm_add_tu2),
    path('xiugai/<str:question_id>/', mysql.sql_xiugai, name='xiugai'),
    url(r'^xiugai2/$', mysql.sql_xiugai1),
    url(r'^xiugai3/$', mysql.sql_xiugai2),
    url(r'^chuti_tk/$', mycs.chuti_tk),
    url(r'^chuti_tk1/$', mycs.chuti_tk1, name='tiankong'),
    url(r'^chuti_tkbj/$', mycs.chuti_tkbj, name='tiankongbj'),
    path('lsadd/', myls.add_dan1, name='ls_add_dan1'),
    path('lsadd2/', myls.add_dan2, name='ls_add_dan2'),
    path('test1/', myls.timu1, name='ls_timu1'),
    path('test2/', myls.timu2, name='ls_timu2'),
    path('index/', myls.userload, name='userload'),
    path('index2/', myls.userload2, name='userload'),
    path('test30/', myls.timushowall, name='showall'),
    path('jieguo/', myls.timujieguo, name='jieguo'),
    


    
]