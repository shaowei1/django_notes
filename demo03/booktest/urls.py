from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^index/$', views.index, name='inde'),
    url(r'^index/(?P<num>\d)/$', views.index, name='inde')
}
# url使用dict时，不能使用reverse
