from django import template


register = template.Library()


@register.filter(name='get_border')
def get_border_class(value):
    bt_class = {
        "#ffffff": "border-light",
        "#000000": "border-dark",
    }
    try:
        return bt_class[value.text_colour]
    except KeyError:
        return "border-light"
