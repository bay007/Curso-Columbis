from django.db import models
import uuid
from datetime import datetime
# Create your models here.


class Question(models.Model):
    uuid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{str(self.uuid)[:5]}__{self.question_text[:10] }"


class Choice(models.Model):
    uuid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.uuid)[:5]}__{self.choice_text[:10] }"
