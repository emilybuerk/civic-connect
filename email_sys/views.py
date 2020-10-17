

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Template
from .forms import ScratchForm, TemplateForm


# Create your views here.
def prompt(request):
    context = {'templates_list': Template.objects.all()}
    return render(request, 'email_sys/prompt.html', context)

def scratch(request):
    if request.method == "POST":
        form = ScratchForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return HttpResponseRedirect(reverse('email_sys:preview', args=(template.id,)))
    else:
        form = ScratchForm()
        context = {
            'form': form,
        }
        return render(request, 'email_sys/scratch.html', context)


def from_template(request, template_id):
    template = get_object_or_404(Template, pk=template_id)
    if request.method == "POST":
        form = TemplateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return HttpResponseRedirect(reverse('email_sys:preview', args=(template.id,)))
    else:
        form = TemplateForm(name_placeholder=template.title, body_placeholder=template.body)
        context = {
            'form': form,
        }
        return render(request, 'email_sys/scratch.html', context)