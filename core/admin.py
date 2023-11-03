from django.contrib import admin
from django.contrib.auth.models import Group

from core.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
