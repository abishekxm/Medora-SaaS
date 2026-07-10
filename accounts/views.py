from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import (
    urlsafe_base64_encode,
    urlsafe_base64_decode,
)

from .serializers import (
    UserSerializer,
    RegisterSerializer,
    PasswordResetSerializer,
    PasswordResetConfirmSerializer,
)

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class PasswordResetRequestView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            user = User.objects.filter(email=email).first()

            if user:
                token = PasswordResetTokenGenerator().make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))

                # Replace this with email sending in production
                print(
                    f"Password reset link generated: "
                    f"/api/v1/auth/password-reset-confirm/{uid}/{token}/"
                )

            return Response(
                {
                    "message": "If an account with this email exists, a reset link has been processed."
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, uidb64, token):
        serializer = PasswordResetConfirmSerializer(data=request.data)

        if serializer.is_valid():
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)

            except (
                TypeError,
                ValueError,
                OverflowError,
                User.DoesNotExist,
            ):
                user = None

            if (
                user is not None
                and PasswordResetTokenGenerator().check_token(user, token)
            ):
                user.set_password(serializer.validated_data["new_password"])
                user.save()

                return Response(
                    {"message": "Password has been reset successfully."},
                    status=status.HTTP_200_OK,
                )

            return Response(
                {"error": "Invalid token or user ID."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        print("REGISTER REQUEST:", request.data)
        return super().post(request, *args, **kwargs)
    
from django.contrib.auth.models import User
from django.http import JsonResponse

def create_admin(request):
    if User.objects.filter(username="admin").exists():
        return JsonResponse({"message": "Admin already exists"})

    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="Admin@123"
    )

    return JsonResponse({"message": "Admin created successfully"})