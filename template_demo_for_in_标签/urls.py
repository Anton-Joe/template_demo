"""template_demo_for_in_标签 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.urls import include
from . import views
from car import views as cviews

urlpatterns = [
    path('', views.index),
    path('movie', views.movie, name='movie'),
    path('movie/detail/<movie_id>/<category_id>', views.movie_detail, name='movie_detail'),
    path('movie/detail2', views.movice_detail_2, name='movie_detail_2'),
    path('cut', views.cut_view, name='cut_view'),
    path('add', views.add_view, name='add_view'),
    path('date', views.date_view, name='date_view'),
    path('default_view', views.default_view, name='default_view'),
    path('car', cviews.index, name='car_index'),
    path('includeapp', include('includeApp.urls')),
    path('extendapp', include('extend_demo_app.urls'))
]
