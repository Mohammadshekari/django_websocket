from django.contrib import admin
from chat.models import ChatMessage, Chat

admin.site.register(ChatMessage)
admin.site.register(Chat)
