# Generated by Django 4.2.2 on 2024-06-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0008_remove_subscription_sign_of_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="sign_of_subscription",
            field=models.BooleanField(default=False, verbose_name="Признак подписки"),
        ),
    ]
