from django import template
import re

register = template.Library()

@register.filter
def to_num(value):
    numbers = re.findall(r'\d+', value)
    if not numbers :
        return ''
    else :
        for idx,number in enumerate(numbers) :
            numbers[idx] = number + '번 출구'
        return ", ".join(numbers)

