from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    topic = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    score = models.IntegerField(default=0)

    total_questions = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.user.username} - {self.topic}"