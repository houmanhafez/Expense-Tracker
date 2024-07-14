from django import forms
from .models import Expense, Month


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["date", "category", "amount", "month"]


class MonthForm(forms.ModelForm):
    class Meta:
        model = Month
        fields = ["name"]
