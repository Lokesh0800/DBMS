# Generated by Django 4.0.5 on 2023-01-31 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0008_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Client_name',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Company_address',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Company_contact',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Company_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Company_name',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Company_website',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Service_opted',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Service_status',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
