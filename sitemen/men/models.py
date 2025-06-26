from django.db import models
from django.db.models import PROTECT, CASCADE
from django.shortcuts import reverse

# Create your models here.

class Men(models.Model):
    title = models.CharField()
    slug = models.SlugField(unique=True, max_length=255, db_index= True, default='')
    content = models.TextField(blank = True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default=True)
    photo = models.ImageField(upload_to = 'image_for_men', default = None, blank = True, null = True)
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

    class Meta:
        ordering = ['-time_create']


class Category(models.Model):
    name = models.CharField()
    slug = models.SlugField(max_length=255, blank=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories", kwargs={"cat": self.slug})





