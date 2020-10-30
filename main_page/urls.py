from django.urls import path

from . import views

app_name = 'main_page'#namespace (is this for the templates??)
urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('email/', views.email, name='email_page'),
    path('resources/', views.ResourceView.as_view(), name='resource_page'),
    path('resources/submit/', views.resource_submit_form, name='resource_submit_page'),
    path('resources/submit/processing', views.submit_resource, name='resource_submission'),
    path('resources/submit/thanks', views.resource_thanks, name='resource_thanks'),
    path('contact-list/', views.contact_list, name='contact_list')
]