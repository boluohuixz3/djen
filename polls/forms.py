from django import forms-------->必须引入
from django import formsclass 
login_form(forms.Form):    
#新增一个form类，在form中加入元素，比如下面，加入两个字符串，客户端的label名称定义，输入的最大值（指定后无法输入更多字符），输入的最小值（指定后若少于该值会提示），指定错误信息（这是一个字典类型）    
    username=forms.CharField(label='用户名',min_length=2,max_length=5,error_messages={"required":"用户名不能为空"});#即使什么都没有设置，它也已经帮你设置了默认不能为空    
    pwd=forms.CharField(label="密码");