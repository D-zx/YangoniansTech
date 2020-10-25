from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Service(models.Model):
	TOWNSHIP = [
		('တာမွေ', 'တာမွေ'),
		('မင်္ဂလာတောင်ညွ့န်', 'မင်္ဂလာတောင်ညွ့န်'),
		('ဗိုလ်တစ်ထောင်', 'ဗိုလ်တစ်ထောင်'),
		('လှိုင်သာယာ', 'လှိုင်သာယာ'),
		('အင်းစိန်', 'အင်းစိန်'),
		('အရှ့ဒဂုံ', 'အရှ့ဒဂုံ'),
		('ရွှေပြည်သာ', 'ရွှေပြည်သာ'),
		('တောင်ဒဂုံ', 'တောင်ဒဂုံ'),
		('တောင်ဥက္ကလာပ', 'တောင်ဥက္ကလာပ'),
		('ကြည့်မြင်တိုင်', 'ကြည့်မြင်တိုင်'),
		('မှော်ဘီ', 'မှော်ဘီ'),
		('အလုံ', 'အလုံ'),
		('ရန်ကင်း', 'ရန်ကင်း'),
		('လှိုင်', 'လှိုင်'),
		('မြောက်ဥက္ကလာပ', 'မြောက်ဥက္ကလာပ'),
		('သာကေတ', 'သာကေတ'),
		('မရမ်းကုန်း', 'မရမ်းကုန်း'),
		('သာကေတ', 'သာကေတ'),
		(' တွံတေး', ' တွံတေး'),
		('ဒေါပုံ', 'ဒေါပုံ'),
		('သန်လျင်', 'သန်လျင်'),
		('ကော့မှူး', 'ကော့မှူး'),
		('ကွမ်းခြံကုန်း', 'ကွမ်းခြံကုန်း'),
		('ဗဟန်း', 'ဗဟန်း'),
	]
	REGION =[
		('Yangon', 'Yangon'),
		('Mandalay', 'Mandalay'),
	]
	C_TYPE = [
		('Q', 'Quarantine Center'),
		('hospital', 'Hospital'),
		('public', 'Public Clinic'),
		('fever', 'Fever Clinic'),
		('volunteer', 'Volunteer'),
		('amulance', 'Amulance'),
		('hotline', 'Hotline'),
	]
	name = models.CharField(max_length=200, default='')
	location = models.CharField(max_length=200, default='')
	township = models.CharField(max_length=200, choices=TOWNSHIP, default="KAMAYUT")
	region = models.CharField(max_length=200, choices=REGION, default="KAMAYUT")
	s_type = models.CharField(max_length=200, choices=C_TYPE, default="Public")
	phone = ArrayField(models.CharField(max_length=200), blank=True)
	description = models.TextField(max_length=500, default='', blank=True)

	def __str__(self):
		return self.name

	def is_open(self):
		today = datetime.date.today().isoweekday()
		time = datetime.datetime.now().strftime('%H:%M:%S')
		for day in self.openinghour_set.all():
			if (day.days == today) and (day.from_hour.strftime('%H:%M:%S')<= time < day.to_hour.strftime('%H:%M:%S')):
				return "<span class='new badge teal lighten-2' data-badge-caption='Opening Now'></span>"
		return "<span class='new badge red lighten-2' data-badge-caption='Closed Now'></span>"

	def address(self):
		return self.location +', '+ self.township +', ' + self.region


class OpeningHour(models.Model):
	DAYS = [
	(1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
    (8, "All Days"),
    ]
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	days = models.IntegerField(('All Days'), choices=DAYS)
	from_hour = models.TimeField()
	to_hour = models.TimeField()

	def __str__(self):
		return ("%(days)s (%(from_hour)s - %(to_hour)s)") % {
		'days': self.get_days_display(),
		'from_hour': self.from_hour,
		'to_hour': self.to_hour
		}


class FAQ(models.Model):
	question = models.CharField(max_length=200, default='')
	answer = models.TextField(max_length=500, default='')
