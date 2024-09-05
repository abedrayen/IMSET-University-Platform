from django.urls import path
from .views import api_root, UserCreateView, UserLoginView, UserLogoutView, UserProfileView, PasswordResetView, ChangePasswordView, TwoFactorAuthView, ChangeLanguageView

urlpatterns = [
    path('', api_root, name='api_root'),  # Root endpoint
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('two-factor-auth/', TwoFactorAuthView.as_view(), name='two-factor-auth'),
    path('change-language/', ChangeLanguageView.as_view(), name='change-language'),
]
