# Generated by Django 5.1.6 on 2025-02-11 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='software',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
