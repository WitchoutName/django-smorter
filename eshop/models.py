from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
import datetime, json


def item_img_path(instance, filename):
    return f"media/shop/{instance.item.shop.id}/items/{instance.item.id}/{filename}"


def shop_img_path(instance, filename):
    return f"media/shop/{instance.id}/image/{filename}"


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
        # return f"{self.name} ({''.join([f'{y}, ' for y in set([x.type for x in self.permissions.all()])])[:-2]})"
        return self.name


class SmorterUser(models.Model):
    user = models.OneToOneField(User, unique=True, null=False, blank=False, on_delete=models.CASCADE)
    groups = models.ManyToManyField(SmorterGroup)

    class Meta:
        ordering = ["user"]

    def __str__(self):
        return f"{self.user.username}"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        SmorterUser.objects.create(user=instance)


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class ShipmentMethod(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Shop(models.Model):
    owner = models.ForeignKey(SmorterUser, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField()
    admin_group = models.OneToOneField(SmorterGroup, null=True, blank=True, on_delete=models.SET_NULL)
    payment_methods = models.ManyToManyField(PaymentMethod, blank=False, null=False)
    shipment_methods = models.ManyToManyField(ShipmentMethod, blank=False, null=False)
    datetime = models.DateTimeField(default=datetime.datetime.now, blank=True)
    image = models.ImageField(upload_to=shop_img_path, null=True, blank=True)

    class Meta:
        ordering = ["owner"]

    def __str__(self):
        return f"{self.owner} - {self.title}"


class Item(models.Model):
    shop = models.ForeignKey(Shop, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=9, blank=False, null=False)
    specs = models.CharField(max_length=1000, default={})

    class Meta:
        ordering = ["shop", "path"]

    def __str__(self):
        return f"{self.shop.title}/{self.path}/{self.title}"

    def set_specs(self, value):
        self.specs = json.dumps(value)

    def get_specs(self):
        return json.loads(self.specs)


class ItemImage(models.Model):
    item = models.ForeignKey(Item, null=False, blank=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=item_img_path, null=False, blank=False)
    alt = models.CharField(max_length=50, default="item_image")

    def __str__(self):
        return f"{self.item.id} - {self.alt}"


class Order(models.Model):
    customer = models.ForeignKey(SmorterUser, null=False, blank=False, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, null=False, blank=False)
    choices = models.CharField(max_length=1000, default={}, null=False, blank=False)
    shop = models.ForeignKey(Shop, null=False, blank=False, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, null=True, blank=False, on_delete=models.SET_NULL)
    shipment_method = models.ForeignKey(ShipmentMethod, null=True, blank=False, on_delete=models.SET_NULL)

    class OrderStatus(models.TextChoices):
        WP = 'WP', _('Waiting for payment')
        OA = 'OA', _('Order accepted')
        WS = 'WS', _('Waiting to be shipped')
        WD = 'WD', _('Waiting for delivery')
        AC = 'AC', _('Arrival confirmed')

    status = models.CharField(max_length=15, choices=OrderStatus.choices, null=False, blank=False, default=OrderStatus.WP)

    class Meta:
        ordering = ["customer", "shop"]

    def __str__(self):
        return f"{self.customer} - {self.shop.title}"

    def set_choices(self, value):
        self.choices = json.dumps(value)

    def get_choices(self):
        return json.loads(self.choices)
    

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