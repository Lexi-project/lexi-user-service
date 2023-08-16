from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userapp.models import Account, User

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Account)
