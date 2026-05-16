from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('add/', views.add_item, name='add_item'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('<int:pk>/quantity/', views.update_quantity, name='update_quantity'),
]