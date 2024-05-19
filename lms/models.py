from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(
        upload_to="lms/courses", verbose_name="Превью", blank=True, null=True
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    preview = models.ImageField(
        upload_to="lms/lessons", verbose_name="Превью", blank=True, null=True
    )
    url = models.CharField(
        max_length=100, verbose_name="Ссылка на видео", blank=True, null=True
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", blank=True, null=True)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title
