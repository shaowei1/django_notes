from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def set_cookies(request):
    response = HttpResponse('ok')
    # 临时cookies, browse close will not to save this cookie1
    response.set_cookie('python', 'yanxinyue', max_age=None)
    response.set_cookie('ruby', 'xiaojia', max_age=3600)  # one hour
    return response


def get_cookies(request):
    cookie1 = request.COOKIES.get('python', None)
    cookie2 = request.COOKIES.get('ruby', None)
    print(cookie1, cookie2)
    return HttpResponse('ok')


def set_session(request):
    request.session['one'] = '1'
    request.session['two'] = '2'
    request.session['three'] = '3'
    return HttpResponse('保存session数据成功')


def get_session(request):
    one = request.session.get('one')
    two = request.session.get('two')
    three = request.session.get('three')
    text = 'one=%s, two=%s, three=%s' % (one, two, three)
    return HttpResponse(text)
