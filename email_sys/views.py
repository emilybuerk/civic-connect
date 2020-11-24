

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
    
    email = None
    if 'email' in request.POST.keys():
        email = request.POST['email']
    
    context = {'drop_down_list':Template.objects.all(), 'email_text':email}
    return render(request, 'email_sys/email_view.html',context)


def email_success_view(request):
    email = ""
    text_body = ""
    subject = ""
    if 'email' in request.POST.keys():
        email = request.POST['email']

    if 'text_body' in request.POST.keys():
        text_body = request.POST['text_body']
    
    if 'subject' in request.POST.keys():
        subject = request.POST['subject']

    context = {'email_text':email, 'text_body': text_body, 'subject':subject}
    return render(request, 'email_sys/email_sent.html', context)


def prompt(request):
    context = {'templates_list': Template.objects.all()}
    return render(request, 'email_sys/email_prompt.html', context)


def customize_template(request, template_id):
    template = Template.objects.get(pk=template_id)
    context = {
        'template_parameters': template.get_parameters(),
        'param_values': {}
    }
    return render(request, 'email_sys/template_customize.html', context)


def unique_template_view(request, template_id):
    email = None
    if 'email_dropdown' in request.POST.keys():
        email = request.POST['email_dropdown']
    context = {
        'template': Template.objects.get(pk=template_id), 
        'urlbody': urllib.parse.quote(Template.objects.get(pk=template_id).body),
        'urltitle': urllib.parse.quote(Template.objects.get(pk=template_id).title),
        'email_text': email}
    return render(request, 'email_sys/template_email.html',context)#scratch_email.html')



# def from_template(request, template_id):
#     template = get_object_or_404(Template, pk=template_id)
#     return render(request, 'email_sys/template_email.html')