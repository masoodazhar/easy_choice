# Generated by Django 3.2.7 on 2021-12-02 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_auto_20211202_2058'),
        ('frontend', '0006_buypolicyhealth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buypolicyhealth',
            name='policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.policyhealth'),
        ),
    ]
