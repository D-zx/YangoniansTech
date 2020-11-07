from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseNotFound
from django.test import SimpleTestCase, override_settings
from django.urls import path
# Create your views here.
from django.views.generic import (TemplateView, ListView, DetailView,FormView,
                                        CreateView, UpdateView, DeleteView)

class HomePage(TemplateView):
	template_name = 'home/index.html'

	def get(self, request):
		return redirect('charity:home')



def page_not_found_view(request, exception=None):
	return render(request, 'errors/404.html', status=404)

def error_view(request, exception=None):
	return render(request, 'errors/500.html', status=500)

def permission_denied_view(request, exception=None):
	return render(request, 'errors/403.html', status=403)

def bad_request_view(request, exception=None):
	return render(request, 'errors/400.html', status=400)