from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Expense, Month
from .forms import ExpenseForm
from django.utils.dateparse import parse_date


def index(request):
    months = Month.objects.all()
    return render(request, "expenses/index.html", {"months": months})


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


def add_month(request):
    if request.method == "POST":
        form = MonthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = MonthForm()
    return render(request, "expenses/add_month.html", {"form": form})


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
