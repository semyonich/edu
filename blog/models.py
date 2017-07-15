from django.db import models
from django.contrib.auth.models import User

from utils import get_file_path

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.FileField(upload_to=get_file_path, blank=True, null=True)
    author = models.ForeignKey(User, blank=True)
    def __str__(self):
        return '{} | {} | {}'.format(self.title, self.body, self.author.username)