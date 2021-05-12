# Generated by Django 3.2 on 2021-04-15 09:12

from django.db import migrations, models
import django.db.models.deletion
import eshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0006_alter_shop_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('path', models.TextField(blank=True, null=True)),
                ('price', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['shop', 'path'],
            },
        ),
        migrations.AlterModelOptions(
            name='smorterpermission',
            options={'ordering': ['type']},
        ),
        migrations.RemoveField(
            model_name='smorteruser',
            name='email',
        ),
        migrations.AddField(
            model_name='shop',
            name='image',
            field=models.ImageField(null=True, upload_to=eshop.models.shop_img_path),
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=eshop.models.item_img_path)),
                ('alt', models.CharField(default='item_image', max_length=50)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.shop'),
        ),
    ]
