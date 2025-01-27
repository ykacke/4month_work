from django.urls import path
from . import views
from .views import AboutMyPetsView, AboutMeView, DateTimeView, MovieListView, MovieDetailView, BookSearchView

urlpatterns = [
    path('movie_list/', MovieListView.as_view(), name='movie_list'),
    path('movie_detail/int:id/', MovieDetailView.as_view(), name='movie_detail'),
    path('about_me/', AboutMeView.as_view(), name='about_me'),
    path('about_my_pets/', AboutMyPetsView.as_view(), name='about_my_pets'),
    path('current_time/', DateTimeView.as_view(), name='current_time'),
    path('search/', views.SearchView.as_view(), name='search'),
]
