# Generated by Django 2.0.4 on 2018-04-30 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Predictor', '0005_auto_20180423_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='passenger_type',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
