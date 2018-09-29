from rest_framework import viewsets, mixins, status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from usermanagement.models import User
from usermanagement.serializers import UserPracticeSerializer, SalutationSerializer, PasswordResetSerializer, TokenSetPasswordSerializer, TokenizedProfileSerializer, UserPatientSerializer, ProviderProfileSerializer
from usermanagement.permissions import IsCreationOrIsAuthenticatedOrHasValidToken
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.conf import settings
from datetime import datetime

class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.id)

    def get_serializer_class(self):
        if self.request.user.is_patient:
            return UserPatientSerializer
        else:
            return UserPracticeSerializer

