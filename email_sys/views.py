

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Template


# Create your views here.


def prompt(request):
    context = {'templates_list': Template.objects.all()}
    return render(request, 'email_sys/email_prompt.html', context)

def scratch(request):
    return render(request, 'email_sys/scratch_email.html')


def from_template(request, template_id):
    template = get_object_or_404(Template, pk=template_id)
    return render(request, 'email_sys/template_email.html')