from django.urls import path
from . import views
app_name = 'includeApp'

urlpatterns = [
    path('',  views.index, name='include_app_index'),
    path('/test', views.test, name='include_app_test')
]