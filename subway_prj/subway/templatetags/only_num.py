from django import template
import re

register = template.Library()

@register.filter
def only_num(value):
    numbers = re.findall(r'\d+', value)
    return numbers[0]

