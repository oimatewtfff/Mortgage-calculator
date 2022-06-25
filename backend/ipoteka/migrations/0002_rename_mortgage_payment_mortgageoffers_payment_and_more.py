# Generated by Django 4.0.5 on 2022-06-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipoteka', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mortgageoffers',
            old_name='mortgage_payment',
            new_name='payment',
        ),
        migrations.RenameField(
            model_name='mortgageoffers',
            old_name='mortgage_rate',
            new_name='rate_max',
        ),
        migrations.AddField(
            model_name='mortgageoffers',
            name='payment_max',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mortgageoffers',
            name='payment_min',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mortgageoffers',
            name='rate_min',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='mortgageoffers',
            name='term_max',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mortgageoffers',
            name='term_min',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mortgageoffers',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
