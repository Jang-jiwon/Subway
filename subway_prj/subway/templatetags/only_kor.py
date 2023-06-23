from django import template
import re
register = template.Library()

@register.filter
def only_kor(value):
    value = value.replace(" ","")
    regex = re.compile(r'^[가-힣]*$')
    return regex.match(value)