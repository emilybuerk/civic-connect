from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

class HomeView(generic.ListView):
    template_name = 'main_page/home_view.html'
    def get_queryset(self):#what does this do again???
        return None

def home(request):
    template = loader.get_template('main_page/home_view.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    return HttpResponse("This is login page")

def email(request):
    return HttpResponse("This is email page")