
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
# from rest_framework.viewsets import ModelViewSet

from users.models import Payments, User
from users.serializers import PaymentsSerializer, UserSerializer


class PaymentsListApiView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["payment_method"]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["payment_method"]
    ordering_fields = ["payments_date"]


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
