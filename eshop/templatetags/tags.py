import json

from django import template
from ..views import is_shop_admin

register = template.Library()


@register.filter(name='item_image')
def item_image(value):
    if len(value):
        return value[0].image.url


@register.filter(name='widther')
def widther(value):
    if value:
        return value[0].image_width > value[0].image_height


@register.filter(name='item_title')
def item_title(title, search):
    return title.replace(search, f"<span class='searched'>{search}</span>") if search else title


@register.filter(name='item_specs')
def item_specs(item):
    options = json.loads(item.item.specs)
    print(options, item.specs)
    return [[attr, json.loads(item.specs)[i]] for i, attr in enumerate(options)]


@register.filter(name='cart_total')
def cart_total(cart):
    return sum([x.item.price * x.count for x in cart.items.all()])


@register.filter(name='range')
def range_tag(value):
    return range(value)


@register.filter(name='attr')
def attr(value, arg):
    if value:
        return value.get(arg)


@register.filter(name='jsonParse')
def json_parse(value):
    if value:
        return json.loads(value)


@register.filter(name="is_admin")
def is_admin(user, shop):
    return is_shop_admin(user, shop)


