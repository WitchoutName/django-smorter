from django import template

register = template.Library()

@register.filter(name='item_image')
def item_image(value):
    if len(value):
        return value[0].image.url


@register.filter(name='item_title')
def item_title(title, search):
    return title.replace(search, f"<span class='searched'>{search}</span>") if search else title

@register.filter(name='range')
def range_tag(value):
    return range(value)