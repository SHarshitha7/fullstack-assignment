# Generated by Django 5.0.2 on 2025-03-13 09:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="conversation",
            name="summary",
            field=models.TextField(blank=True, null=True),
        ),
    ]
