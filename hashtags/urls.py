from django.urls import path
from . import views

urlpatterns = [
    path('tags/', views.all_products, name='all_tags'),
    path('tags_male', views.male_products, name='tag_detail'),
    path('tags_female', views.female_products, name='tag_detail'),
]