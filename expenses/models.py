from django.db import models

class Month(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Expense(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.ForeignKey(Month, on_delete=models.CASCADE, related_name='expenses')

    def __str__(self):
        return f"{self.date} - {self.category} - {self.amount}"
