from django import template
register = template.Library()
import re


@register.simple_tag(name='removeSpaceAndCapitalize')
def removeSpaceAndCapitalize(value):
    return value.replace(' ','').lower().lower()

@register.simple_tag(name='choeck_condition')
def choeck_condition(value):
    return False
register.filter('choeck_condition', choeck_condition)