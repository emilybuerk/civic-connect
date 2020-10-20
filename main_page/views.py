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


def resource_submit_form(request):
    template_name = 'main_page/resource_submit.html'
    context = {
        'issue_list': Issue.objects.all(),
    }

    return render(request, template_name, context)


def home(request):
    template = loader.get_template('main_page/home_view.html')
    context = {}
    return HttpResponse(template.render(context, request))


# Redirect landing page to civcconnect
def landing_page(request):
    return HttpResponseRedirect('/civicconnect/')


def email(request):
    return HttpResponse("This is email page")


def resource_thanks(request):
    template_name = 'main_page/resource_thanks.html'
    context = {}

    return render(request, template_name, context)


def submit_resource(request):
    # Get POST data
    error = False
    try:
        title = request.POST['title']
        if len(title) < 1:
            error = 'Please enter a resource title'
    except KeyError:
        error = 'Please enter a resource title'
    try:
        url = request.POST['url']
        if len(url) < 1:
            error = 'Please enter a url'
    except KeyError:
        error = 'Please enter a url'
    submitter_id = request.POST['submitter']
    anonymous = False
    if 'anonymous' in request.POST.keys():
        anonymous = True

    # Error Handling
    if error:
        return render(request, 'main_page/resource_submit.html', {
            'issue_list': Issue.objects.all(),
            'error_message': error
        })

    # Add resource database
    issue = Issue.objects.get(pk=request.POST['issue'])
    issue.resource_set.create(title=title, url=url, status='P', submitter_id=submitter_id, anonymous=anonymous)
    return HttpResponseRedirect(reverse('main_page:resource_page'))
