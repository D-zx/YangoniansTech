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
    return "အမျိုးအစားအားလုံး"

@register.filter
def services_title(title):
	if title == "hotline":
		return "Call Center"
	elif title == "homeservice":
		return "home service"
	elif title == "public":
		return "Public Clinic"
	elif title == "fever":
		return "fever clinic"
	elif title == "tele":
		return "tele consulation"
	elif title:
		return title
	else:
		return "All Service"

