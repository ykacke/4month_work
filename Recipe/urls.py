from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('recipe/add/', views.add_recipe, name='add_recipe'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
]
