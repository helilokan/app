from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">我的第一个网页</h1>'
    line2 = '<img src="https://img0.baidu.com/it/u=2109596793,204974589&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500"width = 1200>'
    return HttpResponse(line1+line2)
