from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


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

    # There are two ways doing the redirection after post creation. If we want to see the post created
    # in its own view, we use the following,
    # If we want it to just jump to home page, go to blog/views and see success_url
    # def get_absolute_url(self):
    #     # this is going to send us to the newly created post page after creating it
    #     # return reverse('post-detail', kwargs={'pk':self.pk})
