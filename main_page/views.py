from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Issue, UserProfile, government_officials
from django.contrib.auth.models import User

# Create your views here.


class LoginView(generic.TemplateView):
    template_name = "main_page/login.html"


def resources(request):
    template = loader.get_template('main_page/resources.html')

    # Initialize context
    context = {'issue_list': [], 'resource_library': {}, 'top_issues': []}
    keyword = ''
    if 'filter' in request.GET.keys():
        keyword = request.GET['filter']

    # Get issues in proper order
    all_issues = list(Issue.objects.all())
    all_issues.sort(key=lambda x: x.name)
    try:
        current_user = User.objects.get(username=request.user)
        top_issues = list(UserProfile.objects.get(user_id=current_user.id).top_issues.all())
        top_issues.sort(key=lambda x: x.name)
    except (User.DoesNotExist, UserProfile.DoesNotExist) as err:
        top_issues = []
    sorted_issues = []
    for issue in top_issues:
        sorted_issues.append(issue)
    for issue in all_issues:
        if issue not in sorted_issues:
            sorted_issues.append(issue)

    # Check if resource matches search filter
    for issue in sorted_issues:
        visible_resources = []
        for resource in issue.active_resources():
            if keyword.lower() in resource.title.lower():
                visible_resources.append(resource)
        # Only display issue if it has at least one visible resource
        if len(visible_resources) > 0:
            context['issue_list'].append(issue)
            context['resource_library'][issue.name] = visible_resources
            if issue in top_issues:
                context['top_issues'].append(issue.name)
    return HttpResponse(template.render(context, request))


def resource_submit_form(request):
    template_name = 'main_page/resource_submit.html'
    context = {
        'issue_list': Issue.objects.all(),
    }

    return render(request, template_name, context)


def home(request):
    template = loader.get_template('main_page/home_view.html')
    context = {}
    try:
        current_user = User.objects.get(username=request.user)
        user_profile = UserProfile.objects.get(user_id=current_user.id)
        context['contacts'] = user_profile.government_officials()
        context['address'] = user_profile.address
    except (User.DoesNotExist, UserProfile.DoesNotExist) as err:
        context['needs_address'] = True
    try:
        context['contacts'] = government_officials(request.POST['address'])
        context['address'] = request.POST['address']
        if 'save_info' in request.POST.keys():
            # Save address in user's profile
            current_user = User.objects.get(username=request.user)
            user_profile = UserProfile(user_id=current_user.id, address=request.POST['address'])
            user_profile.save()
        context['needs_address'] = False
    except KeyError:
        pass
    return HttpResponse(template.render(context, request))


def contact_list(request):
    template = loader.get_template('main_page/contact_list.html')
    context = {}
    try:
        current_user = User.objects.get(username=request.user)
        user_profile = UserProfile.objects.get(user_id=current_user.id)
        context['contacts'] = user_profile.government_officials()
    except (User.DoesNotExist, UserProfile.DoesNotExist) as err:
        try:
            context['contacts'] = government_officials(request.POST['address'])
        except KeyError:
            context['needs_address'] = True
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
    if int(request.POST['issue']) < 1:
        error = 'Please select an issue'
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
    return HttpResponseRedirect(reverse('main_page:resource_thanks'))
