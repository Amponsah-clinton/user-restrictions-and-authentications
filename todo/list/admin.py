from django.contrib import admin
from .models import message

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'approved', ]

admin.site.register(message, MessageAdmin)
    