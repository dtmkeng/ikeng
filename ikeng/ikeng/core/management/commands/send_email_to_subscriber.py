from django.core.management.base import BaseCommand, CommandError
from core.models.subscriber import SubscriberModel

from django.core import mail


class Command(BaseCommand):
    help = "This is commnad show send email"

    def handle(self, *args, **options):
        try:
            emails = []
            subscribers = SubscriberModel.objects.all()
            for subscriber in subscribers:
                emails.append(subscriber.email)
            self.send_email(emails)
        except Exception as e:
            raise CommandError(e)

    def send_email(self, emails):
        connection = mail.get_connection()

        connection.open()

        emails = mail.EmailMessage(
            'Hello Subscriber',
            'Have a good day',
            'ikeng@test.com',
            emails,
            connection=connection,
        )
        emails.send()

        connection.close()
