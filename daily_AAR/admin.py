from django.contrib import admin

# Register your models here.

from daily_aar.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)