# Generated by Django 3.2.7 on 2021-11-21 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20211120_2352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='policytravel',
            old_name='days10',
            new_name='days_10',
        ),
        migrations.RenameField(
            model_name='policytravel',
            old_name='days122',
            new_name='days_122',
        ),
        migrations.RenameField(
            model_name='policytravel',
            old_name='days15',
            new_name='days_15',
        ),
        migrations.RenameField(
            model_name='policytravel',
            old_name='days152',
            new_name='days_152',
        ),
        migrations.RenameField(
            model_name='policytravel',
            old_name='days180',
            new_name='days_180',
        ),
        migrations.RenameField(
            model_name='policytravel',
            old_name='days21',
            new_name='days_21',
        ),
        migrations.RenameField(
            model_name='policytravel',
            old_name='days31',
            new_name='days_31',
        ),
        migrations.RenameField(
            model_name='policytravel',
            old_name='days62',
            new_name='days_62',
        ),
        migrations.RenameField(
            model_name='policytravel',
            old_name='days7',
            new_name='days_7',
        ),
        migrations.RenameField(
            model_name='policytravel',
            old_name='days92',
            new_name='days_92',
        ),
        migrations.AddField(
            model_name='policytravel',
            name='family_amount_10',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='family_amount_122',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='family_amount_15',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='family_amount_152',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='family_amount_180',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='family_amount_21',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='family_amount_31',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='family_amount_62',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='family_amount_7',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='family_amount_92',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='individual_amount_10',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='individual_amount_122',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='individual_amount_15',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='individual_amount_152',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='individual_amount_180',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='individual_amount_21',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='individual_amount_31',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='individual_amount_62',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='individual_amount_7',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='individual_amount_92',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]