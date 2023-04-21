from django import template

register = template.Library()

# filter to perform value multiplication inside template
@register.filter(name='multiply')
def multiply(value, arg):
    return value * arg