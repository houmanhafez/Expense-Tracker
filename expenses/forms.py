from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'category', 'amount', 'currency']
        widgets = {
            'currency': forms.TextInput(attrs={'placeholder': 'e.g., USD, EUR'}),
        }
        initial = {
            'currency': 'EUR',
        }
