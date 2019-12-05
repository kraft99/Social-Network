from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.urls import reverse
# Create your views here.


def search_user(request):
	if request.is_ajax():
		query = request.GET.get('query')
		if not q is None:
			print('hey')
		return JsonResponse({'ajax':True})
