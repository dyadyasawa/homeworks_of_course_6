
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.course = Course.objects.create(title="Математика", description="Точная наука")
        self.lesson = Lesson.objects.create(title="Урок_1", description="Введение", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lms:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("title"), self.lesson.title
        )

    def test_lesson_create(self):
        url = reverse("lms:lesson_create")
        data = {
            "title": "Урок_10"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.filter(title="Урок_1").count(), 1
        )

    def test_lesson_update(self):
        url = reverse("lms:lesson_update", args=(self.lesson.pk,))
        data = {
            "title": "Урок_10"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("title"), "Урок_10"
        )

    def test_lesson_delete(self):
        url = reverse("lms:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse("lms:lesson_list")
        response = self.client.get(url)
        data = response.json()
        # print(data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        result = {
                  "count": 1,
                  "next": None,
                  "previous": None,
                  "results": [
                             {
                              "id": self.lesson.pk,
                              "title": self.lesson.title,
                              "description": self.lesson.description,
                              "preview": None,
                              "url": None,
                              "course": self.course.pk,
                              "owner": self.user.pk
                              }
                              ]
                }
        self.assertEqual(
            data, result
        )


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.course = Course.objects.create(title="Математика", description="Точная наука", owner=self.user)
        self.lesson = Lesson.objects.create(title="Урок_1", description="Введение", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("title"), self.course.title
        )

    # def test_course_create(self):
    #     url = "http://127.0.0.1:8000/lms/"  # reverse("lms:course-list")
    #     data = {
    #         "title": "Физика",
    #         "description": "Наука о движении",
    #         "owner": self.user
    #     }
    #     response = self.client.post(url, data)
    #
    #     self.assertEqual(
    #         response.status_code, status.HTTP_201_CREATED
    #     )
    #     self.assertEqual(
    #         Course.objects.all().count(), 2
    #     )

    def test_course_update(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        data = {
            "title": "География"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("title"), "География"
        )

    def test_course_delete(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_course_list(self):
        url = reverse("lms:course-list")
        response = self.client.get(url)
        data = response.json()
        # print(data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "lesson": [
                        {
                            "id": self.lesson.pk,
                            "title": self.lesson.title,
                            "description": self.lesson.description,
                            "preview": None,
                            "url": None,
                            "course": self.course.pk,
                            "owner": self.user.pk
                        }

                    ],
                    "lesson_count": 1,
                    "subscription": False,
                    "title": self.course.title,
                    "description": self.course.description,
                    "preview": None,
                    "owner": self.user.pk
                }
            ]
        }
        self.assertEqual(
            data, result
        )
