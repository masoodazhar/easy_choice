# Generated by Django 3.2.7 on 2021-11-30 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20211129_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyhealth',
            name='hospitalization',
            field=models.CharField(choices=[('0.6 lac to 2 lac', '0.6 lac to 2 lac'), ('2 lac to 5 lac', '2 lac to 5 lac'), ('5 lac to 10 lac', '5 lac to 10 lac')], max_length=50),
        ),
    ]
