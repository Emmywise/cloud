from django.contrib import admin
from .models import Profile
#from .form import DocumentForm
# Register your models here.
#from django.contrib.auth.admin import UserAdmin
#class customUserAdmin(UserAdmin):
#    upload_form = DocumentForm

admin.site.register(Profile)