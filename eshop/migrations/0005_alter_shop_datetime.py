# Generated by Django 3.2 on 2021-04-14 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0004_alter_shop_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
