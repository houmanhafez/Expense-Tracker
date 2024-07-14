from django.urls import path
from . import views
from .views import index, add_expense, edit_expense


urlpatterns = [
    path("", views.index, name="index"),
    path("add_expense/", views.add_expense, name="add_expense"),
    path("add_month/", views.add_month, name="add_month"),
    path("expense-data/", views.expense_data, name="expense_data"),
    path("edit/<int:expense_id>/", edit_expense, name="edit_expense"),
]
