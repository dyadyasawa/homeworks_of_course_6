
import datetime
from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

from lms.models import Course, Subscription
from users.models import User


@shared_task
def check_last_update_date(pk):
    current_date = datetime.datetime.now()  # Текущая дата
    course = Course.objects.get(pk=pk)
    if course:

        if not course.last_update_date or int(course.last_update_date.timestamp()) < int(current_date.timestamp()):
            # course.last_update_date = None
            # course.save()
            print(f"Нынешняя дата вот такая: {current_date}")
            print(f"Дата из базы данных: {course.last_update_date}")

            course.last_update_date = current_date
            course.save()

            print("Пора!")
        else:
            print("Рановато.")



    # subscription = Subscription.objects.filter(course_id=pk, sign_of_subscription=True)
    # user_id_list = []
    # if subscription:
    #     for sub in subscription:
    #         user_id_list.append(sub.user_id)
    #     if len(user_id_list) > 0:
    #         user_email = []
    #         for item in user_id_list:
    #             email = User.objects.get(pk=item).email
    #             user_email.append(email)
    #         # return user_email
    #         print(user_email)


@shared_task
def privet(pk):
    print("***** ВСЕМ ПРИВЕТ! *****")
    # print(pk)
