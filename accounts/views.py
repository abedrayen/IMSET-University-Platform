from django.contrib.auth import authenticate, login, logout
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer, UserLoginSerializer
import random
import string
from django.http import JsonResponse


def generate_verification_code(length=6):
    return ''.join(random.choices(string.digits, k=length))


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# User login view
class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk, 'username': user.username})

# User logout view
class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# Password reset view
class PasswordResetView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        # Implement the password reset logic here (e.g., sending a reset email)
        return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')
        if not user.check_password(current_password):
            return Response({'error': 'Current password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()
        return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)

class TwoFactorAuthView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        code = generate_verification_code()
        expiration_time = timezone.now() + timedelta(minutes=10)  # Code expires in 10 minutes

        user.two_factor_code = code
        user.two_factor_code_expires_at = expiration_time
        user.save()


        send_mail(
            'Your Two-Factor Authentication Code',
            f'Your verification code is {code}. It will expire in 10 minutes.',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

        return Response({'message': 'Two-factor authentication setup. Check your email for the verification code.'}, status=status.HTTP_200_OK)


class VerifyTwoFactorCodeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        code = request.data.get('code')

        if not code:
            return Response({'error': 'Verification code is required'}, status=status.HTTP_400_BAD_REQUEST)

      
        if (user.two_factor_code == code and
            user.two_factor_code_expires_at >= timezone.now()):
     
            user.two_factor_code = None
            user.two_factor_code_expires_at = None
            user.save()
            return Response({'message': 'Two-factor authentication verified successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid or expired verification code'}, status=status.HTTP_400_BAD_REQUEST)


class ChangeLanguageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        language = request.data.get('language')
        if language not in ['en', 'fr', 'es']:  # Example languages
            return Response({'error': 'Unsupported language'}, status=status.HTTP_400_BAD_REQUEST)
        translation.activate(language)
        request.session[translation.LANGUAGE_SESSION_KEY] = language
        return Response({'message': _('Language changed successfully')}, status=status.HTTP_200_OK)


def api_root(request):
    return JsonResponse({
        'register': 'api/accounts/register/',
        'login': 'api/accounts/login/',
        'logout': 'api/accounts/logout/',
        'profile': 'api/accounts/profile/',
        'password-reset': 'api/accounts/password-reset/',
        'change-password': 'api/accounts/change-password/',
        'two-factor-auth': 'api/accounts/two-factor-auth/',
        'verify-two-factor-code': 'api/accounts/verify-two-factor-code/',
        'change-language': 'api/accounts/change-language/',
    })
