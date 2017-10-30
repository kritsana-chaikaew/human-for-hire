from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime

class Report(models.Model):
    report_no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100, default='report subject')
    detail = models.CharField(max_length=2000, default='report detail')
    init_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.subject)
