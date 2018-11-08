from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello/(\d)/(\d)/$', views.hello, name='hello'),
    url(r'^test_middle/$', views.demo_view),
]
