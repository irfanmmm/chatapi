from django.shortcuts import get_object_or_404
from api.v1.main.serializer import OpponentList, SerialzerChats, SerialzerListofUsers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from main.models import CustomUser
from main.models import Chats


#  LIST OF USERS
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def userslist(request):
    # exclude(pk=request.user.pk)
    instance = CustomUser.objects.exclude(pk=request.user.pk)
    # print(users)

    context = {"request": request}

    serializer = SerialzerListofUsers(instance, context=context, many=True)

    response_data = {
        "status_code": 6000,
        "message": "SuccessFull",
        "data": serializer.data,
    }
    return Response(response_data)


# CHAT
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def comment(request, reciver=None):
    user_id = request.user.id
    comment = request.data.get("comment")

    try:
        user_instance = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        responsedata = {"status_code": 6001, "message": "User not found"}
        return Response(responsedata, status=404)

    try:
        # Assuming opent_user_id is a field in your Chats model
        chat_instance = Chats.objects.create(
            comment=comment, user_id=reciver, opent_user_id=user_id
        )

        serializer = SerialzerChats(chat_instance)

        responsedata = {
            "status_code": 6000,
            "message": "Successful",
            "data": serializer.data,
        }
        return Response(responsedata)
    except Exception as e:
        responsedata = {"status_code": 500, "message": str(e)}
        return Response(responsedata, status=500)


# LIST MY OF CHATS
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def chatslist(request, reciver=None):
    user_id = request.user.id
    try:
        # reciver=request.user.get()
        print("reciver")
        instance = Chats.objects.filter(user_id=reciver, opent_user_id=user_id)
    except:
        return Response({"status_code": 404, "message": "Chat not found"})

    context = {"request": request}

    try:
        serializer = SerialzerChats(instance, context=context, many=True)
        response_data = {
            "status_code": 6000,
            "message": "Successful",
            "data": serializer.data,
        }
        return Response(response_data)
    except Exception as e:
        return Response({"status_code": 500, "message": str(e)})


# OPPONENT CHAT
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def oponentchat(request, reciver=None):
    try:
        user_id = request.user.id
        # Get messages sent by the receiver to the reciver
        messages_received = Chats.objects.filter(user_id=user_id, opent_user_id=reciver)

        if not messages_received.exists():
            return Response({"status_code": 404, "message": "Chat not found"})

    except Chats.DoesNotExist:
        return Response({"status_code": 404, "message": "Chat not found"})

    context = {"request": request}

    try:
        serializer_received = SerialzerChats(
            messages_received, context=context, many=True
        )

        response_data = {
            "status_code": 200,
            "message": "Successful",
            "data": serializer_received.data,
        }
        return Response(response_data)
    except Exception as e:
        return Response({"status_code": 500, "message": str(e)})

    # print(instance)
