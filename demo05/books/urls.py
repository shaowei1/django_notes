from django.conf.urls import url
from django.contrib import admin
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^books/$', views.BooksView.as_view()),
    url(r'^books/(?P<id>\d+)/$', views.BookView.as_view()),
]
# route = DefaultRouter()
# route.register('books', views.BookViewSet)
# urlpatterns += route.urls
