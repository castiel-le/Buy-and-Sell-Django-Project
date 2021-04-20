from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # to change the time to be constant after post creation, set DateTimeField to auto_now_add=True
    date_posted = models.DateTimeField(default=timezone.now)
    # CASCADE - if the user deleted, posts of that user are deleted too
    # use SET() to pass an author (i.e. "author deleted")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title