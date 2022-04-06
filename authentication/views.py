from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework import Response
from rest_framework.views import APIView
from authentication.serializers import UserSerializer
from django.contrib.auth import get_user_model

from authentication.services import send_message

User= get_user_model()


class RegisterAPIView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            send_message(user)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)


class ActivateUserAccount(APIView):
    def get(self, request, activation_code):
        user =User.objects.get(activation_code=activation_code)
        user.is_active =True
        user.activation_code =''
        user.save()
        return redirect('index.html')
