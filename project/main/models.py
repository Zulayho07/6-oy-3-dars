from django.db import models
from datetime import datetime

class Category(models.Model):
    name=models.CharField(max_length=155, unique=True)

    def __str__(self):
        return self.name


class News(models.Model):
    name=models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    published_year = models.PositiveSmallIntegerField(default=datetime.now().year)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
