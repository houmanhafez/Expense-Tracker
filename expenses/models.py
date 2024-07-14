from django.db import models


class Month(models.Model):
    name = models.CharField(max_length=50)

    @property
    def total_expenses(self):
        return self.expenses.aggregate(total=models.Sum('amount'))['total'] or 0

    def __str__(self):
        return self.name


class Expense(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.ForeignKey(Month, related_name='expenses', on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, default='USD') 


    def __str__(self):
        return f'{self.date} - {self.category} - ${self.amount}'