from django.urls import path, include

from . import views

app_name = 'main_page'
urlpatterns = [
    path('', views.home, name='home_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('email/', views.email, name='email_page'),
    path('resources/', views.resources, name='resource_page'),
    path('resources/submit/', views.resource_submit_form, name='resource_submit_page'),
    path('resources/submit/processing', views.submit_resource, name='resource_submission'),
    path('resources/submit/thanks', views.resource_thanks, name='resource_thanks'),
    path('resources/top-issues/update', views.update_top_issues, name='update_top_issues'),
    path('contact-list/', views.contact_list, name='contact_list'),
    path('accounts/', views.generic.TemplateView.as_view(template_name="main_page/login.html")),
    path('accounts/', include('allauth.urls'))
]
