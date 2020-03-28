from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'username':'anton'
    }
    return render(request, 'include_index.html', context=context)


def test(request):
    return render(request, 'include_test.html')

