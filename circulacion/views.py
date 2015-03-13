from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from circulacion.models import *

# Create your views here.
def home(request):
	template="index.html"
	return render_to_response(template)