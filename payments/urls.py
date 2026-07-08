from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    PaymentViewSet,
    CreateRazorpayOrder,
    VerifyRazorpayPayment,
)
router = DefaultRouter()
router.register(r'payments', PaymentViewSet)
urlpatterns = router.urls + [
    path(
        "create-order/<int:appointment_id>/",
        CreateRazorpayOrder.as_view(),
        name="create-razorpay-order",
    ),
    path(
    "verify-payment/",
    VerifyRazorpayPayment.as_view(),
    name="verify-payment",
),

]
