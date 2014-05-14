from django.contrib import admin
from django.contrib.auth.models import User
from accounts.models import UserProfile


class UserProfileInline(admin.TabularInline):
    model = UserProfile

admin.site.unregister(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserProfileInline,
    ]

