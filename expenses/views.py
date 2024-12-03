from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotAuthenticated

class ExpenseManagerViewSet(APIView):
    def get(self, request):
        return Response({"hello":"response"}, status=status.HTTP_200_OK)
