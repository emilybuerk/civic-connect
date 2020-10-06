from django.urls import path

from . import views

app_name = 'main_page'#namespace (is this for the templates??)
urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home_page'),
    path('login/', views.LoginView.as_view(), name = 'login_page'),
    path('email/', views.email, name = 'email_page')
]