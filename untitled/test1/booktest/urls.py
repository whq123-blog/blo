#自己创建的
from django.conf.urls import url
from  django.urls import path
from . import views
urlpatterns = [
    url(r'^$', views.index),

    url(r'^book/([0-9]+)/$', views.detail, name="detail"),#^。。开始，$。。结束

]#name 是啥