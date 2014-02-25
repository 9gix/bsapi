from django.contrib import admin
from django.contrib.auth.models import User
from accounts.models import UserDetail


class UserDetailInline(admin.TabularInline):
    model = UserDetail

admin.site.unregister(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserDetailInline,
    ]

