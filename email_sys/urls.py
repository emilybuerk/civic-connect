from django.urls import path

from . import views

app_name = 'email_sys'
urlpatterns = [
    path('prompt/', views.EmailView.as_view(), name='prompt_page'),
    path('scratch/',views.scratch, name='scratch_page'),
    path('<int:template_id>/template/', views.From_Template_View.as_view(), name='template_email_page'),

]