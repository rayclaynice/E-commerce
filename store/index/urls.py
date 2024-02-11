from django.urls import path
from . import views



urlpatterns= [
    #e-commerce main page
    path('', views.home, name='index'),

    #e-commerce individual product page
    path('product/<slug:product_slug>/', views.product_details, name='product_details'),

    # E-commerce individual category page
    path('search/<slug:category_slug>/', views.category_details, name='category_details'),

]
 