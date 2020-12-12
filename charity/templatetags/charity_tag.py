from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter
def type_list(list, req):
	value = req.get('type')
	for x , y in list:
		if value == 'homeservice':
			return "အိမ်သို့ ပင့်ဆောင်နိုင်သော ဆရာဝန်များ"
		elif x == value:
			return "ဆက်သွယ်နိုင်သော %sများ"%y
	return "အမျိုးအစားအားလုံး"

@register.filter
def services_title(name):
	title = name.get('type')
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

@register.filter
def township_list(list, value):
	township = value.get('township')
	if township is not None:
		for x , y in list:
			if township == "":
				return "မြို့နယ်အားလုံး"
			elif x == township:
				return "ရွေးချယ်လိုက်သော "+y + "မြို့နယ်"
	else:
		return "မြို့နယ်အားလုံး"
