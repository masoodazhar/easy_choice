# Generated by Django 3.2.7 on 2021-11-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_alter_policyhealth_hospitalization'),
    ]

    operations = [
        migrations.AddField(
            model_name='policyhealth',
            name='maternity_cover_price',
            field=models.FloatField(default=0),
        ),
    ]
