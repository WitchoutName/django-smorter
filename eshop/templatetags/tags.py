from django import template

register = template.Library()

@register.filter(name='item_image')
def item_image(value):
    if len(value):
        return value[0].image.url