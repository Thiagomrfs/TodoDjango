from django.db import models
from django.utils.timezone import now

class Todo(models.Model):
    added_date = models.DateTimeField(default=now, editable=False)
    text = models.CharField(max_length=200)
