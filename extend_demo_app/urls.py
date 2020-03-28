from django.urls import path
from . import views
app_name = 'extend_demo'

urlpatterns = [
    path('', views.index, name='extend_demo_index'),
    path('/test', views.test, name='extend_demo_test')
]