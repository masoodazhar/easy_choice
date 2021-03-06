# Generated by Django 3.2.7 on 2021-11-21 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20211121_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policytravel',
            name='family_amount',
        ),
        migrations.RemoveField(
            model_name='policytravel',
            name='individual_amount',
        ),
        migrations.AddField(
            model_name='policytravel',
            name='family_amount_amt',
            field=models.FloatField(default=1, verbose_name='Family Amount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='family_amount_sa',
            field=models.CharField(default=1, max_length=100, verbose_name='Family Amount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='individual_amount_amt',
            field=models.FloatField(default=1, verbose_name='Individual Aamount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policytravel',
            name='individual_amount_sa',
            field=models.CharField(default=1, max_length=100, verbose_name='Individual Aamount'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_10',
            field=models.FloatField(verbose_name='Family Amount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_122',
            field=models.FloatField(verbose_name='Family Amount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_15',
            field=models.FloatField(verbose_name='Family Amount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_152',
            field=models.FloatField(verbose_name='Family Amount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_180',
            field=models.FloatField(verbose_name='Family Amount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_21',
            field=models.FloatField(verbose_name='Family Amount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_31',
            field=models.FloatField(verbose_name='Family Amount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_62',
            field=models.FloatField(verbose_name='Family Amount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_7',
            field=models.FloatField(verbose_name='Family Amount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_92',
            field=models.FloatField(verbose_name='Family Amount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_10',
            field=models.FloatField(verbose_name='Individual Aamount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_122',
            field=models.FloatField(verbose_name='Individual Aamount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_15',
            field=models.FloatField(verbose_name='Individual Aamount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_152',
            field=models.FloatField(verbose_name='Individual Aamount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_180',
            field=models.FloatField(verbose_name='Individual Aamount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_21',
            field=models.FloatField(verbose_name='Individual Aamount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_31',
            field=models.FloatField(verbose_name='Individual Aamount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_62',
            field=models.FloatField(verbose_name='Individual Aamount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_7',
            field=models.FloatField(verbose_name='Individual Aamount'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_92',
            field=models.FloatField(verbose_name='Individual Aamount'),
        ),
    ]
