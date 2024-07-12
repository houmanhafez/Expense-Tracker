from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('add_month/', views.add_month, name='add_month'),
    path('edit_expense/<int:pk>/', views.edit_expense, name='edit_expense'),  # New URL pattern
]
