# meiduo_mall

# 获取图书列表数据

PATH: /books/

METHOD: GET

Success: 200

Response Data: 

```python
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "btitle": "西游记",
        "bpub_date": "2018-09-14",
        "bread": 0,
        "bcomment": 20,
        "bsales": 0,
        "bprice": "10.00"
    },
    ...
]  
```



# 实现图书列表的分页

PATH: /books/?page=1&page_size=3

METHOD: GET

Success: 200

Response Data:

```python
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 16,
    "next": "http://127.0.0.1:8000/books/?page=2&page_size=3",
    "previous": null,
    "results": [
        {
            "id": 1,
            "btitle": "西游记",
            "bpub_date": "2018-09-14",
            "bread": 0,
            "bcomment": 20,
            "bsales": 0,
            "bprice": "10.00"
        },
        {
            "id": 2,
            "btitle": "水浒传",
            "bpub_date": "2018-09-12",
            "bread": 0,
            "bcomment": 30,
            "bsales": 0,
            "bprice": "21.00"
        },
        {
            "id": 3,
            "btitle": "大话西游",
            "bpub_date": "2008-09-12",
            "bread": 12,
            "bcomment": 12,
            "bsales": 0,
            "bprice": "11.00"
        }
    ]
}
```



# 实现图书按销量进行排序

PATH: /books/?ordering=-bsales

METHOD: GET

Success: 200

Response Data:

```python
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
[
    {
        "id": 13,
        "btitle": "逻辑回归",
        "bpub_date": "2018-09-03",
        "bread": 100,
        "bcomment": 200,
        "bsales": 300,
        "bprice": "23.00"
    },
    {
        "id": 12,
        "btitle": "线性回归",
        "bpub_date": "2015-09-18",
        "bread": 76,
        "bcomment": 45,
        "bsales": 123,
        "bprice": "34.00"
    },
    {
        "id": 16,
        "btitle": "tensorflow",
        "bpub_date": "2016-09-16",
        "bread": 36,
        "bcomment": 56,
        "bsales": 67,
        "bprice": "34.00"
    },
    ...
]    
```



# 实现图书价格进行排序

PATH: /books/?ordering=bprice

METHOD: GET

Success: 200

Response Data:



```python

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "btitle": "西游记",
        "bpub_date": "2018-09-14",
        "bread": 0,
        "bcomment": 20,
        "bsales": 0,
        "bprice": "10.00"
    },
    {
        "id": 4,
        "btitle": "红楼梦",
        "bpub_date": "2012-09-14",
        "bread": 11,
        "bcomment": 11,
        "bsales": 0,
        "bprice": "10.50"
    },
    {
        "id": 3,
        "btitle": "大话西游",
        "bpub_date": "2008-09-12",
        "bread": 12,
        "bcomment": 12,
        "bsales": 0,
        "bprice": "11.00"
    },
    ...
]    
```

# 类视图

```python
# views.py
from django.shortcuts import render

# Create your views here.
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from booksManager.models import Books
from booksManager.serializers import BookSerializers


class PageUum(PageNumberPagination):
    page_size_query_param = 'page_size'


class BooksModelViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializers

    pagination_class = PageUum
    filter_backends = [OrderingFilter]
    ordering_fields = ('bsales', 'bprice')

    pass
```

```python
# serializers.py
from rest_framework import serializers
from booksManager.models import Books


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
```

```python
# urls.py
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [

]

route = DefaultRouter()
route.register('books', views.BooksModelViewSet)
print(route.urls)
urlpatterns += route.urls
```