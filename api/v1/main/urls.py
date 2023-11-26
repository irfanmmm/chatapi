from django.urls import path
from api.v1.main import views
from chat import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.userslist),
    path("comment/<int:reciver>/", views.comment),
    path("chatslist/<int:reciver>/", views.chatslist),
    path("oponentchat/<int:reciver>/", views.oponentchat),
]
