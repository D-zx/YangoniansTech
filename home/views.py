from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import (TemplateView, ListView, DetailView,FormView,
                                        CreateView, UpdateView, DeleteView)

class HomePage(TemplateView):
	template_name = 'home/index.html'

	def get(self, request):
		return redirect('charity:home')
