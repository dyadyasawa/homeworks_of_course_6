from django.urls import path
# from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import PaymentsListApiView
app_name = UsersConfig.name

# router = SimpleRouter()
# router.register("", CourseViewSet)

urlpatterns = [
    path("payment/", PaymentsListApiView.as_view(), name="payment_list"),

    # path("payment/detail/<int:pk>/", PaymentsRetrieveApiView.as_view(), name="payment_detail"),
    # path("payment/create/", PaymentsCreateApiView.as_view(), name="payment_create"),
    # path("payment/update/<int:pk>/", PaymentsUpdateApiView.as_view(), name="payment_update"),
    # path("payment/delete/<int:pk>/", PaymentsDestroyApiView.as_view(), name="payment_delete"),
]

# urlpatterns += router.urls
