from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('checkout/', views.checkout, name='checkout'),
    path('buy/', views.buy, name='buy')
]