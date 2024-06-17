
import datetime
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from lms.models import Course, Lesson, Subscription
from lms.paginations import CustomPagination
from lms.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from users.permissions import IsModerators, IsOwner

from lms.tasks import privet


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPagination

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsModerators,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModerators | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModerators | IsOwner,)
        return super().get_permissions()

    # @action(detail=True, methods=("patch",))
    # def update_date(self, pk, request, *args, **kwargs):
        # partial = kwargs.pop('partial', False)
        # instance = self. get_object()
        # date = instance.last_update_date
        # print(date)
        # instance.last_update_date = datetime.datetime.now()
        # serializer = self.get_serializer(instance, data=request.data)  #, partial=partial)
        # serializer.is_valid(raise_exception=True)
        # self.perform_update(serializer)
        # sending_mail.delay(instance.id, date)
        # return Response(serializer.data)

    # @action(detail=False, methods=("patch",))
    def perform_update(self, serializer):
        instance = serializer.save()
        privet.delay(instance.id)
        return instance


class LessonCreateApiView(CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (~IsModerators, IsAuthenticated,)


class LessonListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerators | IsOwner,)


class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerators | IsOwner,)


class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsOwner | ~IsModerators,)


class SubscriptionCreateAPIView(CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Subscription.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")
        course = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course)

        # print(user)
        # print(course_id)
        # print(course)

        if subs_item.exists():
            subs_item.delete()  # Удаляем подписку
            message = 'подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course)  # Создаем подписку
            message = 'подписка добавлена'
            Subscription.sign_of_subscription = True

        return Response({"message": message})
