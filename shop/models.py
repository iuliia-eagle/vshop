from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class BlogSingle(models.Model):
    header = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_number = models.PositiveIntegerField(default=0)
    # image = models.ImageField()

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('blog', kwargs={'pk': self.pk})
# Create your models here.

# class Product(models.Model):
#     name = models.TextField(max_length=100)
#     # image = models.ImageField()
#     price = models.PositiveIntegerField(default=0)
#     discount = models.PositiveIntegerField(default=0)
#     price_sale = models.PositiveIntegerField(default=0)