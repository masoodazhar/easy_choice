# Generated by Django 3.2.7 on 2021-12-02 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_auto_20211201_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyhealth',
            name='family_kids_amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='policyhealth',
            name='family_parent_amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='policyhealth',
            name='family_price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
