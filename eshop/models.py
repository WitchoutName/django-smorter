from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
import datetime, enum


class SmorterPermission(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)

    class PermissionType(models.TextChoices):
        SA = 'SA', _('Shop Admin')
        C = 'C', _('Customer')
        SO = 'SO', _('Shop Owner')
        WA = 'WA', _('Web Admin')

    type = models.CharField(max_length=15, choices=PermissionType.choices, help_text='Select allowed PERMISSION type')

    class Meta:
        ordering = ["type"]

    def __str__(self):
        return f"{self.type} - {self.name}"


class SmorterGroup(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    permissions = models.ManyToManyField(SmorterPermission, blank=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class SmorterUser(models.Model):
    user = models.OneToOneField(User, unique=True, null=False, blank=False, on_delete=models.CASCADE)
    groups = models.ManyToManyField(SmorterGroup)

    class Meta:
        ordering = ["user"]

    def __str__(self):
        return f"{self.user.email}"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        SmorterUser.objects.create(user=instance)


class Shop(models.Model):
    owner = models.ForeignKey(SmorterUser, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    admin_group = models.OneToOneField(SmorterGroup, null=True, on_delete=models.SET_NULL)
    datetime = models.DateTimeField(default=datetime.datetime.now, blank=True)

    class Meta:
        ordering = ["owner"]

    def __str__(self):
        return f"{self.owner} - {self.title}"

"""
class Choice(models.Model):
    idchoice = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'choice'


class Group(models.Model):
    idgroup = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'group'


class GroupHasRights(models.Model):
    group_idgroup = models.TextField(blank=True, null=True)  # This field type is a guess.
    rights_idrights = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'group_has_rights'


class Item(models.Model):
    iditem = models.TextField(blank=True, null=True)  # This field type is a guess.
    shop_brand_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    img = models.TextField(blank=True, null=True)  # This field type is a guess.
    path = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_count = models.TextField(blank=True, null=True)  # This field type is a guess.
    price = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'item'


class Options(models.Model):
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    item_iditem = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'options'


class OptionsHasChoice(models.Model):
    options_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    choice_idchoice = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'options_has_choice'


class Order(models.Model):
    idorder = models.TextField(blank=True, null=True)  # This field type is a guess.
    account_username = models.TextField(blank=True, null=True)  # This field type is a guess.
    payment_method_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    shippment_method_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    shop_brand_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    status_idstatus = models.TextField(blank=True, null=True)  # This field type is a guess.
    create_date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'order'


class OrderHasItem(models.Model):
    order_idorder = models.TextField(blank=True, null=True)  # This field type is a guess.
    item_iditem = models.TextField(blank=True, null=True)  # This field type is a guess.
    count = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'order_has_item'


class OrderHasItemHasOptions(models.Model):
    order_idorder = models.TextField(blank=True, null=True)  # This field type is a guess.
    item_iditem = models.TextField(blank=True, null=True)  # This field type is a guess.
    options_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    selected_value = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'order_has_item_has_options'


class PaymentMethod(models.Model):
    name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'payment_method'


class Person(models.Model):
    account_username = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    group_idgroup = models.TextField(blank=True, null=True)  # This field type is a guess.
    company_name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'person'


class Rights(models.Model):
    idrights = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rights'


class ShippmentMethod(models.Model):
    name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'shippment_method'


class Shop(models.Model):
    brand_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    img = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'shop'


class ShopHasGroup(models.Model):
    shop_brand_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    group_idgroup = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'shop_has_group'


class ShopHasPaymentMethod(models.Model):
    shop_brand_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    payment_method_name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'shop_has_payment_method'


class ShopHasShippmentMethod(models.Model):
    shop_brand_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    shippment_method_name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'shop_has_shippment_method'


class Status(models.Model):
    idstatus = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'status'
"""