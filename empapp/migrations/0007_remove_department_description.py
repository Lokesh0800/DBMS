# Generated by Django 4.0.5 on 2023-01-12 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0006_rename_salary_employees_ctc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='Description',
        ),
    ]
