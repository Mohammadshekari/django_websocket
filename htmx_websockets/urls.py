from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


def chat_view(request, *args, **kwargs):
    return render(request, 'chat.html')


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('allauth.urls')),
    path('chat', chat_view)
]
