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
		context['townships'] = Service._meta.get_field('township').choices
		context['regions'] = Service._meta.get_field('region').choices
		context['types'] = Service._meta.get_field('s_type').choices
		return context

	def get_queryset(self):
		search={}
		township = self.request.GET.get('township') or ''
		region = self.request.GET.get('region') or ''
		name = self.request.GET.get('name') or ''
		s_type = self.request.GET.get('type') or ''
		search['township__contains'] = township
		search['name__contains'] = name
		search['region__contains'] = region
		search['s_type__contains'] = s_type
		queryset = super(ListView, self).get_queryset()
		queryset = queryset.filter(**search).order_by('id')
		return queryset
