from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Event(models.Model):
  title = models.CharField(max_length=200)
  start_time = models.DateTimeField(default=datetime.date.today)
def __str__(self):
  return self.title
@property
def get_html_url(self):
  url = reverse('event_edit', args=(self.id,))
  return f'<p>{self.title}</p><a href="{url}">edit</a>'