from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie_detail/int:id/', views.movie_detail, name='movie_detail'),
    path('about_me/', views.about_me, name='about_me'),
    path('about_my_pets/', views.about_my_pets, name='about_my_pets'),
    path('date_time/', views.date_time, name='date_time'),
    path('search/', views.SearchView.as_view(), name='search'),
]