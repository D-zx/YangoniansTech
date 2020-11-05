from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter
def list_value(list, name='Q'):
    for x , y in list:
        if name == 'homeservice':
            return "အိမ်သို့ ပင့်ဆောင်နိုင်သော ဆရာဝန်များ"
        elif x == name:
            return "ဆက်သွယ်နိုင်သော %sများ"%y
    return "အမျိုးအစားအားအားလုံး"