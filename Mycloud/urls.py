from django.urls import path
from . import views

app_name = 'Mycloud'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'), 
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('delete/<int:pk>/', views.delete_file, name='delete_file'),
    path('imageupload/', views.imageupload, name='imageupload'),
    path('delete_image/<int:pk>/', views.delete_image, name='delete_image')

]
