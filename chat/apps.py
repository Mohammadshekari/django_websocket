from django.apps import AppConfig


class ChatConfig(AppConfig):
    name = 'chat'
    verbose_name = 'Chats'

    def ready(self):
        from .socket import signals
