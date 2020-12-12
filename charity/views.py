from django.shortcuts import render
from .models import Service, FAQ
# Create your views here.
from django.views.generic import (TemplateView, ListView, DetailView,FormView,
                                        CreateView, UpdateView, DeleteView)

class CharityPage(TemplateView):
	template_name = 'charity/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['faqs'] = FAQ.objects.all()
		return context



class ServiceList(ListView):
	model = Service
	template_name = 'charity/list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['types'] = Service._meta.get_field('s_type').choices
		context['townships'] = Service._meta.get_field('township').choices
		context['regions'] = Service._meta.get_field('region').choices
		if self.request.GET.get('cantest'):
			context['canTest'] = 'checked'
		return context

	def get_queryset(self):
		search={}
		township = self.request.GET.get('township') or ''
		region = self.request.GET.get('region') or ''
		name = self.request.GET.get('name') or ''
		s_type = self.request.GET.get('type') or ''
		can_test = self.request.GET.get('cantest')
		if township:
			search['township__iexact'] = township
		if region:
			search['region__iexact'] = region
		if s_type:
			search['s_type__contains'] = s_type
		if can_test:
			search['canTest'] = True
		else:
			search['canTest'] = False
		search['name__contains'] = name
		queryset = super(ListView, self).get_queryset()
		queryset = queryset.filter(**search).order_by('id')
		return queryset
