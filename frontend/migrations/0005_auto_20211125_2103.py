# Generated by Django 3.2.7 on 2021-11-25 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_buypolicytravel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buypolicytravel',
            name='date_of_birth',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='buypolicytravel',
            name='date_of_issue',
            field=models.CharField(max_length=100),
        ),
    ]