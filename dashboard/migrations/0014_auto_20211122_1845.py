# Generated by Django 3.2.7 on 2021-11-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20211121_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='policytravel',
            name='off',
            field=models.IntegerField(blank=True, default=0, verbose_name='off in %, if not leave it as 0'),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='anual_multi_trip',
            field=models.CharField(default='Annual Multi-Trip', max_length=50, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='days_10',
            field=models.IntegerField(default=10, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='days_122',
            field=models.IntegerField(default=122, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='days_15',
            field=models.IntegerField(default=15, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='days_152',
            field=models.IntegerField(default=152, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='days_180',
            field=models.IntegerField(default=180, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='days_21',
            field=models.IntegerField(default=21, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='days_31',
            field=models.IntegerField(default=31, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='days_62',
            field=models.IntegerField(default=62, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='days_7',
            field=models.IntegerField(default=7, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='days_92',
            field=models.IntegerField(default=92, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_10',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_122',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_15',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_152',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_180',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_21',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_31',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_62',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_7',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_92',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_amt',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='family_amount_sa',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_10',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_122',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_15',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_152',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_180',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_21',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_31',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_62',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_7',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_92',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_amt',
            field=models.FloatField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='individual_amount_sa',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='policytravel',
            name='senior_ages',
            field=models.CharField(default='Senior Age Extension for those aged 65-85', max_length=100, verbose_name=''),
        ),
    ]
