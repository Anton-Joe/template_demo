from django.shortcuts import render
from django.http import HttpResponse

context = {
    'Books': [
        '三国演义',
        '水浒传',
        '西南大学'
    ],
    'Books_Info':[
        {
            'book_name':'桑国演义',
            'author':'叶敬轩'
        },
        {
            'book_name': '四国演义',
            'author':'叶敬轩2'
        },
    ],
    'keys':{
        '第一个键': '1',
        '第二个键': '2',
        '第三个键': '3',
    },
    'testwith': 150515,
    '自动转义标签的使用': "<a href='http://www.baidu.com'>测试网页百度</a>",
    'verbatim标签测试': '参数的值为叶敬轩'
}


def index(request):
    return render(request, 'index.html', context=context)


def movie(request):
    return HttpResponse('电影首页')


def movie_detail(request, movie_id, category_id):
    text = "您的电影id是{x}, 电影分类是{c}".format(x=movie_id,c=category_id)
    return HttpResponse(text)


def movice_detail_2(request):
    id = request.GET.get('movie_id')
    return HttpResponse("您的电影id是{x}".format(x=id))


def cut_view(request):
    return render(request, 'cut.html')


def add_view(request):
    context2 = {
        'value1': '100'
    }
    return render(request, 'add.html', context=context2)
