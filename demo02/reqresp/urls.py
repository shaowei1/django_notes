from django.conf.urls import url

from . import views

urlpatterns = [
    # 位置参数传递
    url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),
    # 命名参数传递
    # url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather)
    url(r'^qs/$', views.qs),
    url(r'^get_body/$', views.get_body),
    url(r'^get_body_json/$', views.get_body_json),
    url(r'^get_headers/$', views.get_headers),
    url(r'^demo_response/$', views.demo_response),
    url(r'^demo_view/$', views.demo_view),
    url(r'^getResponse/$', views.getResponse),
    url(r'^json_response/$', views.json_response),
    url(r'^redirect_response/$', views.redirect_response),
]
