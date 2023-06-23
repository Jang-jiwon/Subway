from django import template

register = template.Library()

@register.filter
def getposition(value):
    return 15 + value*68
@register.filter
def getnextposition(value):
    return 15 + (value+1)*68