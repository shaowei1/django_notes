from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^indexview', views.indexview),
    # 注意:
    # url(路径, 执行的函数)
    # url的第二个参数需要是一个函数
    # 我们这里如果传入: views.RegisterView 会发现这个是一个类, 不是一个函数,
    # 所以我们需要调用系统给我们提供的 as_view() 方法

    # 1. 此种方式最简单,但因装饰行为被放置到了url配置中,单看视图的时候无法知道此视图还被添加了装饰器,
    # 不利于代码的完整性,不建议使用。
    # 2. 此种方式会为类视图中的所有请求方法都加上装饰器行为(因为是在视图入口处,分发请求方式前)
    # url(r'^registerview/$', views.my_decorator(views.RegisterView.as_view())), method one, get, post all can call

    url(r'^registerview/$', views.RegisterView.as_view()),

]
