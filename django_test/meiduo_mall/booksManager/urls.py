from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [

]

route = DefaultRouter()
route.register('books', views.BooksModelViewSet)
print(route.urls)
urlpatterns += route.urls
