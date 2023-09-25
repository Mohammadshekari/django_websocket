from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.template.loader import get_template


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        if not self.user.is_authenticated:
            self.close()
            return
        async_to_sync(self.channel_layer.group_add)(
            'user-' + str(self.user.id), self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_discard)(
                'user-' + str(self.user.id), self.channel_name
            )

    def receive(self, text_data=None, bytes_data=None):
        self.user = self.scope['user']
        if not self.user.is_authenticated:
            self.close()
            return
        print('self.user', self.user, )
        print('text_data', text_data, )
        print('bytes_data', bytes_data, )
        self.send('received!')

    def new_message(self, event):
        print('self.snd', event)
        self.send(text_data=event["text"])
