# Generated by Django 5.1.4 on 2025-01-17 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
