from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


def post_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/post_<author>/<filename>
    return 'post_{0}/{1}'.format(instance.author, filename)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # to change the time to be constant after post creation, set DateTimeField to auto_now_add=True
    date_posted = models.DateTimeField(default=timezone.now)
    # CASCADE - if the user deleted, posts of that user are deleted too
    # use SET() to pass an author (i.e. "author deleted")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    image = models.ImageField(default='default_item.jpg', blank=True, upload_to=post_directory_path)

    def __str__(self):
        return self.title
    # There are two ways doing the redirection after post creation. If we want to see the post created
    # in its own view, we use the following,
    # If we want it to just jump to home page, go to blog/views and see success_url
    # def get_absolute_url(self):
    #     # this is going to send us to the newly created post page after creating it
#     # return reverse('post-detail', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        # resizing images because we can, using pillow library mentioned in class
        super(Post, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Images(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="items/images", null=True, blank=True)

    def __str__(self):
        return self.post.title + " Img"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.user)
