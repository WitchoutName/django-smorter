# Generated by Django 3.2 on 2021-06-20 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0021_auto_20210620_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='choices',
        ),
        migrations.CreateModel(
            name='OrderedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specs', models.CharField(default=[], max_length=1000)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eshop.item')),
            ],
        ),
    ]
