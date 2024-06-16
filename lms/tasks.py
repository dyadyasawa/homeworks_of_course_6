
import datetime
from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

from lms.models import Course, Subscription
from users.models import User


@shared_task
def check_last_update_date(pk):
    instance = Course.objects.filter(pk=pk).first()
    if instance:
        if instance.last_update_date:
            if instance.last_update_date < datetime.datetime.now():
                subs = Subscription.objects.filter(course=instance, sign_of_subscription=True)
                if subs.count() > 0:
                    subscribers = []
                    for sub in subs:
                        subscribers.append(User.objects.get(id=sub.user.id).email)
                    send_mail(
                        subject=f"Курс '{instance.title}' обновлен",
                        message=f"В курсе '{instance.name}' произошли изменения",
                        from_email=EMAIL_HOST_USER,
                        recipient_list=subscribers,
                        fail_silently=False,
                    )
