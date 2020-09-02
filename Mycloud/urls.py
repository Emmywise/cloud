from django.urls import path
from . import views


app_name = 'Mycloud'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'), 
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
]
