from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from tuxbot_web.pages.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("name", "email")}),
        (_("Message"), {"fields": ("message", "read", "answered")}),
    )
    list_display = ["id", "name", "email", "created_at", "read", "answered"]
    search_fields = ["id", "name", "email", "created_at", "read", "answered"]
