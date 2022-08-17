from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Account

admin.site.register(Account)

#admin.site.register(Account, UserAdmin)
# Register your models here.


# class AccountInline(admin.StackedInline):
#     model = Account
#     can_delete: False
#     verbose_name_plural = 'Accounts'


# class _CustomizedUserAdmin(UserAdmin):
#     inlines = (AccountInline,)


# admin.site.unregister(User)
# admin.site.register(User, _CustomizedUserAdmin)
