
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from lms.validators import YouTubeValidator
from lms.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        validators = [YouTubeValidator(field="url")]
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lesson = LessonSerializer(source="lesson_set", many=True)  # Выводим список уроков курса
    lesson_count = SerializerMethodField()  # Выводим количество уроков курса

    class Meta:
        model = Course
        fields = "__all__"

    def get_lesson_count(self, instance):  # Выводим количество уроков курса
        return instance.lesson_set.count()
