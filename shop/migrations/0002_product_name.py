# Generated by Django 4.1.7 on 2023-03-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="name",
            field=models.CharField(default="Product", max_length=100),
        ),
    ]