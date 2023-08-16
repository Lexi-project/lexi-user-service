from django.contrib import admin

from userapp.models import Account, User

# Register your models here.
admin.site.register(User)
admin.site.register(Account)
