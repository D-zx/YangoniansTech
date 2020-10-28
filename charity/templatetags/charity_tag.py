from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter
def list_value(list, name='Q'):
    for x , y in list:
    	if x == name:
    		return y
    return 'Fever Clinic'