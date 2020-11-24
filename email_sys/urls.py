from django.urls import path

from . import views

app_name = 'email_sys'
urlpatterns = [
    path('prompt/', views.template_view, name = 'prompt_page'),
    path('<int:template_id>/customize/', views.customize_template, name='template_email_page'),
    path('<int:template_id>/preview/', views.unique_template_view, name='template_preview_page'),
    path('email_success/',views.email_success_view, name = "email_success_page"),

]