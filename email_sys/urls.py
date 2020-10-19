from django.urls import path

from . import views

app_name = 'email_sys'
urlpatterns = [
    path('prompt/', views.prompt, name='prompt_page'),
    path('scratch/',views.scratch, name='scratch_page'),
    path('<int:template_id>/template/', views.from_template, name='template_edit_page'),
    #path('preview/', views.preview,name='preview_page'),
    path('sent/', views.send, name='sent_page')

]