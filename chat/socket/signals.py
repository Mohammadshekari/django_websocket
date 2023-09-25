from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

from chat.models import ChatMessage


@receiver(post_save, sender=ChatMessage)
def sent_message(sender, instance, created, **kwargs):
    print('Sent message ')
    if created:
        # trigger notification to all consumers in the 'user-notification' group
        channel_layer = get_channel_layer()
        for user in instance.chat.users.all():
            group_name = 'user-' + str(user.id)
            event = {
                "type": "new_message",
                "text": json.dumps({
                    'id': instance.id,
                    'sender': {
                        'id': user.id,
                        'fullname': user.get_full_name(),
                    },
                    'message': instance.text
                })
            }
            async_to_sync(channel_layer.group_send)(group_name, event)
