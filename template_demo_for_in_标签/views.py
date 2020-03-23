from django.shortcuts import render


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
    'testwith': 150515
}


def index(request):
    return render(request, 'index.html', context=context)