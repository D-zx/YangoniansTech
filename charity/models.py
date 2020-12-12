from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Service(models.Model):
	TOWNSHIP = [
		('', 'မြို့နယ်အားလုံး'),
		('alone', 'အလုံ'),
		('bahan', 'ဗဟန်း'),
		('botahtaung', 'ဗိုလ်တစ်ထောင်'),
		('dagon', 'ဒဂုံ'),
		('dagon seikkan', 'ဒဂုံဆိပ်ကမ်း'),
		('dala', 'ဒလ'),
		('dawbon', 'ဒေါပုံ'),
		('eastdagon', 'အရှေ့ဒဂုံ'),
		('hlaing', 'လှိုင်'),
		('hmawbi', 'မှော်ဘီ'),
		('hlaingtharyar', 'လှိုင်သာယာ'),
		('insein', 'အင်းစိန်'),
		('kamayut', 'ကမာရွတ်'),
		('kyauktada', 'ကျောက်တံတား'),
		('kyimyindaing', 'ကြည့်မြင်တိုင်'),
		('kawhmu', 'ကော့မှူး'),
		('kunchankone', 'ကွမ်းခြံကုန်း'),
		('lanmadaw', 'လမ်းမတော်'),
		('lattha', 'လသာ'),
		('mayangone', 'မရမ်းကုန်း'),
		('mingalartaungnyunt', 'မင်္ဂလာတောင်ညွ့န်'),
		('mingaladon', 'မင်္ဂလာဒုံ'),
		('northdagon', 'မြောက်ဒဂုံ'),
		('northokkalapa', 'မြောက်ဥက္ကလာပ'),
		('pabedan', 'ပန်ပဲတန်း'),
		('pazundaung', 'ပုဇွန်တောင်'),
		('sanchaung', 'စမ်းချောင်း'),
		('seikkan', 'ဆိပ်ကမ်း'),
		('shwepyithar', 'ရွှေပြည်သာ'),
		('southdagon', 'တောင်ဒဂုံ'),
		('southokkalapa', 'တောင်ဥက္ကလာပ'),
		('tamwe', 'တာမွေ'),
		('tharkayta', 'သာကေတ'),
		('thanlyin', 'သန်လျင်'),
		('tontay', ' တွံတေး'),
		('thingangyun', 'သင်္ဃန်းကျွန်း'),
		('yankin', 'ရန်ကင်း'),
	]

	REGION =[
		('yangon', 'ရန်ကုန်'),
		('mandalay', 'မန္တလေး'),
	]

	C_TYPE = [
		('homeservice', 'ဆရာဝန်အိမ်ပင့်'),
		('hospital', 'ဆေးရုံ'),
		('public', 'ကိုယ်ပိုင်ဆေးခန်း'),
		('fever', 'ဖျားနာဆေးခန်း'),
		('tele', 'Tele Consulation'),
		('ambulance', 'လူနာတင်ကား'),
		('hotline', 'Call Center'),
		('hotel-q', 'Hotel Quarantine'),
		('q', 'Quarantine Center'),
	]
	name = models.CharField(max_length=200, default='')
	location = models.CharField(max_length=200, default='', blank=True)
	township = models.CharField(max_length=200, choices=TOWNSHIP, blank=True)
	region = models.CharField(max_length=200, choices=REGION, default="yangon")
	s_type = models.CharField(max_length=200, choices=C_TYPE, default="public")
	phone = ArrayField(models.CharField(max_length=200), blank=True)
	canTest = models.BooleanField(default=False)
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
		return self.location +'၊ '+ self.get_township_display() +'၊ ' + self.get_region_display()


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

	def __str__(self):
		return self.question
