from django.contrib import admin
from eshop.models import *

admin.site.register(SmorterUser)
admin.site.register(SmorterGroup)
admin.site.register(SmorterPermission)
admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(PaymentMethod)
admin.site.register(ShipmentMethod)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(OrderedItem)
admin.site.register(Address)
