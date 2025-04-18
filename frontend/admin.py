from django.contrib import admin
from .models import ContactMessage
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
from django.contrib.sites.models import Site

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)

admin.site.unregister(ContactMessage)

# admin.site.unregister(SocialAccount)
# admin.site.unregister(SocialApp)
# admin.site.unregister(SocialToken)

admin.site.unregister(Site)
