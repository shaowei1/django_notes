from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^book/$', views.ListView.as_view()),
    url(r'^books/$', views.BooksView2.as_view()),
    url(r'^post/$', views.BooksView.as_view()),
]
