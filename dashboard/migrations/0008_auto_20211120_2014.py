# Generated by Django 3.2.7 on 2021-11-20 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_featureforpolicy_policy'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelCoverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField()),
                ('type', models.CharField(choices=[('individual', 'individual'), ('family', 'family')], max_length=30)),
                ('bliss', models.FloatField(default=0.0)),
                ('secure', models.FloatField(default=0.0)),
                ('schengen', models.FloatField(default=0.0)),
                ('secure_plus', models.FloatField(default=0.0)),
                ('care', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'travelcoverage',
            },
        ),
        migrations.AlterField(
            model_name='policy',
            name='main_coverage',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='policy',
            name='third_party_coverage',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='policy',
            name='value_added_features',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
