# Generated by Django 3.2 on 2021-05-12 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0014_alter_shop_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='eshop.smorteruser'),
            preserve_default=False,
        ),
    ]
