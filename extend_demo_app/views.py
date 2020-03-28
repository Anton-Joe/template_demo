from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'extend_index.html')


def test(request):
    return render(request, 'extent_test.html')