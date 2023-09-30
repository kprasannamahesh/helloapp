from django.contrib import admin

# Register your models here.
from .models import Pages, Posts, Message

admin.site.register(Pages)
admin.site.register(Posts)
admin.site.register(Message)