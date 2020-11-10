

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Template
import urllib


# Create your views here.


# class EmailView(generic.TemplateView):
#     template_name = "email_sys/email_view.html"

# class From_Template_View(generic.TemplateView):
#     template_name = 'email_sys/template_email.html'

#Loads all drop-down templates
def template_view(request):
    context = {'drop_down_list':Template.objects.all()}
    return render(request, 'email_sys/email_view.html',context)

def prompt(request):
    context = {'templates_list': Template.objects.all()}
    return render(request, 'email_sys/email_prompt.html', context)

def unique_template_view(request, template_id):
    context = {'template':Template.objects.get(pk=template_id), 
        'urlbody': urllib.parse.quote(Template.objects.get(pk=template_id).body),
        'urltitle':urllib.parse.quote(Template.objects.get(pk=template_id).title)}
    return render(request, 'email_sys/template_email.html',context)#scratch_email.html')



# def from_template(request, template_id):
#     template = get_object_or_404(Template, pk=template_id)
#     return render(request, 'email_sys/template_email.html')