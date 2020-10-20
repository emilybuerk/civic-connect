from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Issue

# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'main_page/home_view.html'


class LoginView(generic.TemplateView):
    template_name = "main_page/login.html"


class ResourceView(generic.ListView):
    template_name = 'main_page/resources.html'
    context_object_name = 'issue_list'

    def get_queryset(self):
        """ Return a list of all the issues that have resources """
        issue_list = []
        for issue in Issue.objects.all():
            issue_list.append(issue)
        issue_list.sort(key=lambda x: x.name)
        return issue_list


class ResourceSubmitView(generic.ListView):
    template_name = 'main_page/resource_submit.html'
    context_object_name = 'issue_list'

    def get_queryset(self):
        return Issue.objects.all()


def home(request):
    template = loader.get_template('main_page/home_view.html')
    context = {}
    return HttpResponse(template.render(context, request))


# Redirect landing page to civcconnect
def landing_page(request):
    return HttpResponseRedirect('/civicconnect/')


def email(request):
    return HttpResponse("This is email page")
