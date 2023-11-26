from django.contrib import admin

from main.models import Chats, CustomUser, ListofUsers

admin.site.register(Chats)

admin.site.register(ListofUsers)

admin.site.register(CustomUser)

