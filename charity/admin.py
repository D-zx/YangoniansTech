from django.contrib import admin

# Register your models here.
from .models import Service, OpeningHour, FAQ

# admin.site.register(PublicClinic)
# admin.site.register(OpeningHour)

class HourInline(admin.TabularInline):
    model = OpeningHour

class Hour(admin.ModelAdmin):
    inlines = [
        HourInline,
    ]

admin.site.register(Service, Hour)
admin.site.register(FAQ)