from django.urls import path

from . import views

app_name = 'email_sys'
urlpatterns = [
    path('prompt/', views.prompt, name='prompt_page'),
    path('scratch/',views.scratch, name='scratch_page'),
    path('<int:template_id>/template/', views.from_template, name='template_email_page'),

]