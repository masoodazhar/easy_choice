# Generated by Django 3.2.7 on 2021-11-20 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20211120_2310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='policytravel',
            old_name='main_coverage',
            new_name='medical_benefits',
        ),
        migrations.RenameField(
            model_name='policytravel',
            old_name='third_party_coverage',
            new_name='personal_accident_benefits',
        ),
        migrations.RenameField(
            model_name='policytravel',
            old_name='value_added_features',
            new_name='travel_inconvenience_benefits',
        ),
        migrations.AddField(
            model_name='policytravel',
            name='anual_multi_trip',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='days10',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='days122',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='days15',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='days152',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='days180',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='days21',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='days31',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='days62',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='days7',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='days92',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='family_amount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='individual_amount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='senior_ages',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
