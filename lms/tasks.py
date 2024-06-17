
import datetime
from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

from lms.models import Course, Subscription
from users.models import User


@shared_task
def check_last_update_date(pk):

    current_date = datetime.datetime.now()
    Course.objects.update(last_update_date=current_date)
    # course_data = Course.objects.get(pk=pk)
    # date = course_data.last_update_date  # =None
    # print(current_date)
    # print(date)
    # if date is None or date < current_date:
    #     Course.objects.update(last_update_date=current_date)
    #     print("Пора!")
    # else:
    #     print("Рановато.")



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
