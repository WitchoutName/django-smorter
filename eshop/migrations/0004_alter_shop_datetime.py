# Generated by Django 3.2 on 2021-04-14 22:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0003_alter_shop_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 15, 0, 33, 29, 705285)),
        ),
    ]
