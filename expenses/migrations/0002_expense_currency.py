# Generated by Django 5.0.7 on 2024-07-14 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="currency",
            field=models.CharField(default="USD", max_length=3),
        ),
    ]
