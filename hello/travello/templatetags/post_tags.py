from django import template
from ..models import Resume


register = template.Library()


@register.filter
def toarr(value):
    value = [i.strip() for i in value[1:-1].replace('"',"").split(',')]
    return value[:5]