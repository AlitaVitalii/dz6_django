from time import sleep

from celery import shared_task

from django.core.mail import send_mail


@shared_task
def send_email_task(email, text):
    """Sends an email when the feedback form has been submitted."""
    send_mail(
        "Subject",
        text,
        [email],
        ["support@example.com"],
        fail_silently=False,
    )
