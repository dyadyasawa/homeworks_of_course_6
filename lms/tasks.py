
import datetime
from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

from lms.models import Course, Subscription
from users.models import User


@shared_task
def check_last_update_date(pk):
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
            # return user_email
            print(user_email)

    # if Course.objects.filter(pk=pk).exists():  # Course.title
    #     print("Да, такой курс существует!")
    # else:
    #     print("Такого курса нет...")
    # instance = Course.objects.filter(pk=pk).first()
    # if instance:
    #     print("Я существую!")
    # else:
    #     print("Меня нет!")
        # if not instance.last_update_date or instance.last_update_date < datetime.datetime.now():
        #     subs = Subscription.objects.filter(course=instance, sign_of_subscription=True)
        #     if subs.count() > 0:
        #         subscribers = []
        #         for sub in subs:
        #             print(subscribers.append(User.objects.get(id=sub.user.id).email))
                # send_mail(
                #     subject=f"Курс '{instance.title}' обновлен",
                #     message=f"В курсе '{instance.name}' произошли изменения",
                #     from_email=EMAIL_HOST_USER,
                #     recipient_list=subscribers,
                #     fail_silently=False,
                # )


@shared_task
def privet(pk):
    print("***** ВСЕМ ПРИВЕТ! *****")
    # print(pk)
