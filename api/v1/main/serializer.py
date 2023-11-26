import json
from rest_framework.serializers import ModelSerializer
from main.models import CustomUser
from rest_framework import serializers
from django.http import JsonResponse

from main.models import Chats, ListofUsers, OpponentChats


class SerialzerListofUsers(ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        fields = ("id", "username", "user", "user_id" ,"profileimage")
        model = ListofUsers

    def get_user(self, instance):
        return instance.first_name


class SerialzerChats(ModelSerializer):
    user = serializers.SlugRelatedField(
        many=False, slug_field="username", queryset=CustomUser.objects.all()
    )
    opent_user = serializers.SlugRelatedField(
        many=False, slug_field="username", queryset=CustomUser.objects.all()
    )

    class Meta:
        fields = ("id", "user", "opent_user", "comment", "user_id")
        model = Chats

    # def get_first_name(self, instance):
    #     return instance.user.first_name


class OpponentList(ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        fields = ("id", "user", "comment", "user_id")
        model = OpponentChats

    def get_user(self, instance):
        return instance.user.username
