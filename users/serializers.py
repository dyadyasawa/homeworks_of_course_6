
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.models import Payments


class PaymentsSerializer(ModelSerializer):

    class Meta:
        model = Payments
        fields = "__all__"
