from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

# Create your views here.
from django.views.generic.base import View


def indexview(request):
    # 获取请求方法,判断是GET/POST请求
    if request.method == 'GET':
        # 根据不同的请求方式,做不同的操作处理:
        return HttpResponse('indexview get func')
    else:
        # 根据不同的请求方式,做不同的操作处理:
        return HttpResponse('indexview post func')


# define a decorator
# method one
# func = my_decorator(func)
def my_decorator(func):
    # wrapper函数必然会接收一个request对象,因为传入进来的func这个函数肯定会带这个参数
    def wrapper(request, *args, **kwargs):
        print('自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        return func(request, *args, **kwargs)

    return wrapper


def my_decorator2(func):
    def wrapper(request, *args, **kwargs):
        print('decorator2自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        return func(request, *args, **kwargs)

    return wrapper


class BaseView(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = my_decorator(view)
        return view


class BaseView2(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = my_decorator2(view)
        return view


class RegisterView(BaseView, BaseView2, View):
    # 先调用BaseView, then BaseView2
    def get(self, request):
        print('get')

        return HttpResponse('get func')

    def post(self, request):
        print('post')

        return HttpResponse('post func')


# class BaseView(View):
#     @classmethod
#     def as_view(cls, *args, **kwargs):
#         view = super().as_view(*args, **kwargs)
#         view = my_decorator(view)
#         return view
#
#
# class BaseView2(View):
#     @classmethod
#     def as_view(cls, *args, **kwargs):
#         view = super().as_view(*args, **kwargs)
#         view = my_decorator2(view)
#         return view
#
#
# class RegisterView(BaseView, BaseView2):
#     # 先调用BaseView, then BaseView2
#     def get(self, request):
#         print('get')
#
#         return HttpResponse('get func')
#
#     def post(self, request):
#         print('post')
#
#         return HttpResponse('post func')


# method three, who decorate who call
# def my_decorator(func):
#     # wrapper函数必然会接收一个request对象,因为传入进来的func这个函数肯定会带这个参数
#     def wrapper(self, request, *args, **kwargs):
#         print('自定义装饰器被调用了')
#         print('请求路径%s' % request.path)
#         return func(self, request, *args, **kwargs)
#
#     return wrapper

# @method_decorator(my_decorator, name='get')
# @method_decorator(my_decorator, name='dispatch')
# class RegisterView(View):
#
#     # 重写父类的dispatch方法, 因为这个方法被 as_view() 中的 view() 调用
#     # 所以我们对这个方法添加装饰器, 也就相当于对整个类视图的方法添加装饰器.
#     # @method_decorator(my_decorator)
#     # def dispatch(self, request, *args, **kwargs):
#         # 重写父类的这个方法我们不会修改它的任何参数, 所以我们直接调用父类的这个方法即可
#         # 它里面的参数我们也不动它, 直接还传递过去.
#         # return super().dispatch(request, *args, **kwargs)
#
#     # @my_decorator
#     # 在类视图中使用为函数视图准备的装饰器时,不能直接添加装饰器
#     # 需要使用method_decorator将其转换为适用于类视图方法的装饰器。
#     # @method_decorator(my_decorator) 但是我们这种是给单个函数添加的, 而不是类视图中的所有函数,
#     def get(self, request):
#         """处理GET请求,返回注册⻚面"""
#         print('get method')
#         # return render(request, 'register.html')
#         return HttpResponse('get registerview')
#
#     def post(self, request):
#         """处理POST请求,实现注册逻辑"""
#         print('post method')
#         return HttpResponse('这里实现注册逻辑')


pass
