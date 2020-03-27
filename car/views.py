from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'value': '小王'
    }
    return render(request, 'car_index.html', context=context)

