from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    # url(r'^book/$', views.BooksView.as_view()),
    # url(r'^book/(?P<id>\d+)/$', views.BookView.as_view()),
]

## 不要使用字典，因为不是每个url对象都会别解析成键值对


from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()  # 可以处理视图的路由器
router.register(r'books', views.BookInfoViewSet)  # 向路由器中注册视图集
urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
print(urlpatterns)
