from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('detail/<int:item_id>', views.item_detail, name='detail'),
    path('new/', views.new, name='new'),
    path('edit/<int:item_id>', views.edit, name='edit'),
    path('delete/<int:item_id>', views.delete, name='delete'),
]