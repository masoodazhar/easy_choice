# Generated by Django 3.2.7 on 2021-11-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_alter_company_comapny_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='redirect_link',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
