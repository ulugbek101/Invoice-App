import uuid
import datetime
from django.db import models

from app_users.models import Profile


class Invoice(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='owner_invoices')
    sender = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='sender_invoices')
    amount = models.BigIntegerField(default=10_000_000)
    reason = models.TextField(null=True, blank=True)
    is_confirmed = models.BooleanField(default=False)
    until = models.DateTimeField(null=True)

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def get_status(self):
        until_date = datetime.datetime(
            year=self.until.year,
            month=self.until.month,
            day=self.until.day,
            hour=self.until.hour,
            second=self.until.second)
        if until_date < datetime.datetime.now():
            return f'Wasted {str(self.until)}'
        else:
            return f'Not Wasted {str(self.until)}'

    @property
    def calc_invoice_duration(self):
        until = datetime.datetime(year=self.until.year,
                                  month=self.until.month,
                                  day=self.until.day,
                                  hour=self.until.hour,
                                  second=self.until.second
                                  )
        created = datetime.datetime(
            year=self.created.year,
            month=self.created.month,
            day=self.created.day,
            hour=self.created.hour,
            second=self.created.second
        )
        duration = (until - created) + datetime.timedelta(days=1)
        return str(duration.days)

    def __str__(self):
        return f'{self.owner.user.username} - {self.sender.user.username}'


class News(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='news/', null=True)

    def __str__(self):
        return f'{self.title}'
