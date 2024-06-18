
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
        real_date_second = int(current_date.timestamp())
        date_from_db_second = int(course.last_update_date.timestamp())

        # print(real_date_second)
        # print(date_from_db_second)

        if date_from_db_second < real_date_second:

            course.last_update_date = current_date
            course.save(update_fields=["last_update_date"])

            # print("Пора!")
        # else:
        #     print("Рановато.")

            subscription = Subscription.objects.filter(course_id=pk, sign_of_subscription=True)
            user_id_list = []
            if subscription:
                for sub in subscription:
                    user_id_list.append(sub.user_id)
                if len(user_id_list) > 0:
                    user_email = []
                    for item in user_id_list:
                        email = User.objects.get(pk=item).email
                        user_email.append(email)
                    # print(user_email)
                    send_mail(
                        subject=f"Курс '{course.title}' был обновлен.",
                        message=f"В программе курса '{course.title}' произошли изменения.",
                        from_email=EMAIL_HOST_USER,
                        recipient_list=user_email,
                    )


@shared_task
def privet(pk):
    print("***** ВСЕМ ПРИВЕТ! *****")
    # print(pk)
