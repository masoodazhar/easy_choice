# Generated by Django 3.2.7 on 2021-12-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_auto_20211202_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='recomended',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]