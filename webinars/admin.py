from django.contrib import admin
from .models import Webinar

class WebinarAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

admin.site.register(Webinar, WebinarAdmin)

