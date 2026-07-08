from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import razorpay

from .models import Payment
from .serializers import PaymentSerializer
from .services import create_razorpay_order


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.AllowAny]


class CreateRazorpayOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, appointment_id):
        amount = request.data.get("amount")

        result = create_razorpay_order(
            patient=request.user,
            appointment_id=appointment_id,
            amount=float(amount),
        )

        return Response(
            {
                "payment_id": result["payment"].id,
                "order": result["order"],
            }
        )


class VerifyRazorpayPayment(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        razorpay_order_id = request.data.get("razorpay_order_id")
        razorpay_payment_id = request.data.get("razorpay_payment_id")
        razorpay_signature = request.data.get("razorpay_signature")

        client = razorpay.Client(
            auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
        )

        try:
            client.utility.verify_payment_signature(
                {
                    "razorpay_order_id": razorpay_order_id,
                    "razorpay_payment_id": razorpay_payment_id,
                    "razorpay_signature": razorpay_signature,
                }
            )

            payment = Payment.objects.get(
                razorpay_order_id=razorpay_order_id
            )

            payment.razorpay_payment_id = razorpay_payment_id
            payment.razorpay_signature = razorpay_signature
            payment.transaction_id = razorpay_payment_id
            payment.status = "completed"
            payment.save()

            return Response(
                {
                    "message": "Payment verified successfully."
                }
            )

        except Exception as e:
            return Response(
                {
                    "message": "Payment verification failed.",
                    "error": str(e),
                },
                status=400,
            )