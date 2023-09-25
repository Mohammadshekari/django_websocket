import datetime
from random import choices
from django.utils.deconstruct import deconstructible
from django.core.validators import MaxLengthValidator, BaseValidator
from django.db import models
from django.utils.translation import gettext_lazy as _, ngettext_lazy
from django.contrib.auth import get_user_model

User = get_user_model()


class Chat(models.Model):
    class Meta:
        verbose_name = "چت"
        verbose_name_plural = "چت ها"
        permissions = (
            ('can_chat', _('Manage Chats')),
        )
        ordering = ['-last_message_at', '-pk']

    users = models.ManyToManyField(User, related_name='chats', verbose_name='کاربران', blank=True)
    is_deleted = models.BooleanField(default=False, verbose_name=_('is Deleted'))
    last_message_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Last Message at"))
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=_("Created at"))

    def __str__(self):
        return ' - '.join([x.__str__() for x in self.users.all()])

    def unread_count(self, user=None):
        return self.messages.exclude(seen_by=user).count()

    def unread_messages(self, user):
        return self.messages.exclude(seen_by=user)

    def update_last_message(self):
        self.last_message_at = datetime.datetime.now()
        self.save()

    @staticmethod
    def unread_messages_of(user):
        return ChatMessage.objects.filter(chat__users=user, ).exclude(is_seen=user)


class ChatMessage(models.Model):
    class Meta:
        permissions = (
        )
        ordering = ['-created_at']

    chat = models.ForeignKey(Chat, related_name='messages', null=True, on_delete=models.CASCADE, verbose_name=_("Chat"))
    text = models.TextField(verbose_name="متن", blank=True, validators=[MaxLengthValidator(400)])
    sender = models.ForeignKey(User, related_name='chat_messages', null=True, on_delete=models.CASCADE,
                               verbose_name=_("Writer"))
    seen_by = models.ManyToManyField(User, related_name='seen_messages', verbose_name='خوانده شده', blank=True)
    file = models.FileField(upload_to='messages/', blank=True, null=True, verbose_name=_("File"),
                            validators=[])
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=_("Sent at"))

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        self.chat.update_last_message()
