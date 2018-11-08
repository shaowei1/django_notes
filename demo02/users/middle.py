# 中间件模板:
def my_middleware(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行
    print('init called')

    def middleware(request):
        # 在此编写的代码会在每个请求处理视图前被调用
        print('before request called')
        response = get_response(request)
        # 此处编写的代码会在每个请求处理视图之后被调用
        print('after response called')
        return response

    return middleware


def my_middleware2(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行
    print('init2 called')

    def middleware(request):
        # 在此编写的代码会在每个请求处理视图前被调用
        print('before request 2 called')
        response = get_response(request)
        # 此处编写的代码会在每个请求处理视图之后被调用
        print('after response 2 called')
        return response

    return middleware
