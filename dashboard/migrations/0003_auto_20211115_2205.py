# Generated by Django 3.2.7 on 2021-11-15 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_feature_policy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='category',
            field=models.CharField(choices=[('1', 'Main Coverage'), ('2', 'Third Party Coverage'), ('3', 'Value Added Features')], max_length=100),
        ),
        migrations.AlterField(
            model_name='policy',
            name='off',
            field=models.IntegerField(blank=True, default=0, verbose_name='off in %, if not leave it as 0'),
        ),
    ]
