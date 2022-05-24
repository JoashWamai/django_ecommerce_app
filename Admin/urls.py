from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='administrator'),
    path('products/', views.products, name='products'),
    path('productdetails/', views.addproduct, name='addnewproduct'),
    path('productdetails/<str:pk>', views.updateproduct, name='updateproduct'),
    path('statistics/', views.statistics, name='statistics'),
]
