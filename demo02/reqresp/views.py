from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def weather(request, year, city):
    print('city=%s' % city)
    print('year=%s' % year)
    return HttpResponse('OK')


def qs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)  # 3
    print(b)  # 2
    print(alist)
    # ['1', '3']
    return HttpResponse('OK')


def get_body(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')
    print(a, b, alist)
    return HttpResponse('ok')


import json


def get_body_json(request):
    json_bytes = request.body
    json_str = json_bytes.decode()

    # python3.6及以上版本中, json.loads()方法可以接收str和bytes类型
    # 但是python3.5以及以下版本中, json.loads()方法只能接收str, 所以我们的版本如果是
    # 3.5 需要有上面的编码步骤.

    req_data = json.loads(json_str)
    print(req_data['a'])
    print(req_data['b'])
    return HttpResponse('ok')


def get_headers(request):
    print(request.META['CONTENT_LENGTH'])
    print(request.META['CONTENT_TYPE'])
    print()
    print(request.method)
    print(request.user)
    print(request.path)
    print(request.encoding)
    print(request.FILES)
    return HttpResponse("ok")
    '''
    POST
    AnonymousUser
    /reqresp/get_headers/
    None
    <MultiValueDict: {}>
    '''


# 定义一个新的视图函数
def demo_response(request):
    # 定义一个json字符串
    s = '{"name": "python"}'
    # 返回一个HttpResponse响应对象
    return HttpResponse(s, content_type="application/json", status=400)


def demo_view(request):
    # 自定义响应头python，响应值1111
    response = HttpResponse('python')
    response.status_code = 400
    response['python'] = '1111'
    return response


def getResponse(request):
    print(request.path)
    return HttpResponseNotFound('<h1>404 error</h1>')


def json_response(request):
    return JsonResponse({'city': 'beijin', 'subject': 'python'})


def redirect_response(request):
    # redirect需要写全（总  ＋　子）
    return redirect('/static/error.html')
