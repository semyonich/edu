from django.contrib import admin

from core.models import WebsiteConfiguration

from solo.admin import SingletonModelAdmin
# Register your models here.
admin.site.register(WebsiteConfiguration, SingletonModelAdmin)