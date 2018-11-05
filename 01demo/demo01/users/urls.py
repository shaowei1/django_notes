# 从urls模块中导入url
from django.conf.urls import url

# 从当前目录导入我们的视图模块views
from . import views

# urlpatterns是被django自动识别的路由列表变量
urlpatterns = [
    # url(路径, 视图)
    # 从上到下查找，如果不加/$，可能会出现屏蔽
    url(r'^index/$', views.index, name='indexname'),
    url(r'^say/$', views.say, name='sayname'),
    url(r'^sayhello/$', views.sayhello, name='sayhelloname'),
]
