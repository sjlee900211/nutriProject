from django.contrib import admin

# Register your models here.
from accounts.models import User, Standard


class UserAdmin(admin.ModelAdmin):
    fields = ['user_id', 'password', 'name']

admin.site.register(User)
admin.site.register(Standard)

