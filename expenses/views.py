from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Month
from .forms import ExpenseForm, MonthForm


def index(request):
    months = Month.objects.all()
    total_expenses = {
        month: sum(expense.amount for expense in month.expenses.all())
        for month in months
    }
    return render(
        request,
        "expenses/index.html",
        {"months": months, "total_expenses": total_expenses},
    )


def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
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


def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
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
