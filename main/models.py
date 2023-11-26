from django.db import models
from django.contrib.auth.models import AbstractUser
from chat import settings


class CustomUser(AbstractUser):
    profileimage = models.ImageField(upload_to="profileimage/", blank=True, null=True)


class ListofUsers(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    username = models.TextField(default="hellow")
    profileimage = models.ImageField(
        upload_to="profiles/images", default="profiles/images/Burger_Poster_aS7OI8W.png"
    )

    # def __str__(self):
    #     return self.user


class Chats(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="chats_as_user"
    )
    opent_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="chats_as_opent_user",
    )
    comment = models.TextField()


class OpponentChats(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.ForeignKey(Chats, on_delete=models.CASCADE)


class UserList(models.Model):
    name = models.CharField(max_length=255)
