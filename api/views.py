
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.http import HttpResponse
from .models import LbLogin,LbEngg
from django.core import serializers
import urllib2
import json
import datetime

# Create your views here.
def index(request):
	data = LbLogin.objects.all()
	jsondata = serializers.serialize('json', data)
	return HttpResponse(jsondata)

def link_index(request):
	data = LbEngg.objects.all()
	jsondata = serializers.serialize('json', data)
	if request.GET.get('q')=="json":
		return JsonResponse({'status':'ok','response':jsondata})
	elif request.GET.get('q')=="html":
		return HttpResponse(jsondata)
