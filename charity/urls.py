from django.conf.urls import url
from django.urls import path
from .views import CharityPage, ServiceList

app_name = 'charity'
urlpatterns = [
	path('', CharityPage.as_view(), name='home'),
	path('services/', ServiceList.as_view(), name='service-list'),
]