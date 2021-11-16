from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from django.contrib.auth import forms
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from accounts.forms import UserChangeForm, SignUpForm
from accounts.models import User, Standard


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = SignUpForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('user_id', 'name','is_superuser')
    list_display_links = ('user_id',)
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('user_id', 'password')}),
        (('Personal info'),
         {'fields': ('name',
                     'n_code',
                     'height',
                     'weight',
                     'age_category',
                     'gender',
                     'activity',
                     'proper_cal')}),
        (('Permissions'), {'fields': ('is_superuser',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'name', 'password', 'password_check')}
         ),
    )
    search_fields = ('user_id','name')
    ordering = ('-is_superuser',)

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
admin.site.register(Standard)
# admin.site.register(Upload)

