from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    # url(r'^books/$', views.BooksView.as_view()),
    # url(r'^book/(?P<pk>\d+)/$', views.BookView.as_view())

    # ViewSet
    # url(r'^book/$', views.BooksViewSet.as_view({'get': 'list'})),
    # url(r'^book/(?P<pk>\d+)/$', views.BooksViewSet.as_view({'get': 'retrieve'}))

    # ModelViewSet
    # url(r'^book/$', views.BooksModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^book/(?P<pk>\d+)/$',
    #     views.BooksModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
    # 自定义方法
    # url(r'^book/last/$', views.BooksModelViewSet.as_view({'get': 'last'})),
    url(r'^book/(?P<pk>\d+)/read/$', views.BooksModelViewSet.as_view({'put': 'read'}))
    # {'pk':1}
]

# 对视图集自动生成路由
route = DefaultRouter()
route.register(r'book', views.BooksModelViewSet, 'rest_book')
print(route.urls)
urlpatterns += route.urls
