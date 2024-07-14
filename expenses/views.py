from django.shortcuts import render, redirect, get_object_or_404
from django.utils.dateparse import parse_date
from django.db.models import Q
from django.http import JsonResponse
from .models import Expense, Month
from .forms import ExpenseForm
from collections import defaultdict
import json


def index(request):
    expenses = Expense.objects.all().order_by('-date')
    
    expenses_by_category = defaultdict(float)
    expenses_by_month = defaultdict(float)

    for expense in expenses:
        expenses_by_category[expense.category] += float(expense.amount)
        expenses_by_month[expense.date.strftime('%B %Y')] += float(expense.amount)

    grouped_expenses = {}
    for expense in expenses:
        month_name = expense.date.strftime('%B %Y')
        if month_name not in grouped_expenses:
            grouped_expenses[month_name] = []
        grouped_expenses[month_name].append(expense)

    context = {
        'grouped_expenses': grouped_expenses,
        'expenses_by_category': json.dumps(expenses_by_category),
        'expenses_by_month': json.dumps(expenses_by_month)
    }
    return render(request, 'expenses/index.html', context)


def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense_date = form.cleaned_data["date"]
            month_name = expense_date.strftime("%B")
            month, created = Month.objects.get_or_create(name=month_name)
            expense.month = month
            expense.save()
            return redirect("index")
    else:
        form = ExpenseForm()

    return render(request, "expenses/add_expense.html", {"form": form})



def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == "POST":

        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ExpenseForm(instance=expense)

    return render(
        request, "expenses/edit_expense.html", {"form": form, "expense": expense}
    )


def expense_data(request):
    expenses = Expense.objects.all()
    data = {
        "labels": [expense.date for expense in expenses],
        "data": [expense.amount for expense in expenses],
    }
    return JsonResponse(data)


def search_expenses(request):
    query = request.GET.get('query')
    results = Expense.objects.filter(
        Q(category__icontains=query) | 
        Q(currency__icontains=query) |
        Q(amount__icontains=query)
    )
    return render(request, 'expenses/search_results.html', {'results': results})

