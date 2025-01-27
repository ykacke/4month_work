from django.urls import path
from . import views
from .views import AllProductsView, MaleProductsView, FemaleProductsView

urlpatterns = [
    path('products/', AllProductsView.as_view(), name='all_products'),
    path('products/male/', MaleProductsView.as_view(), name='male_products'),
    path('products/female/', FemaleProductsView.as_view(), name='female_products'),
]