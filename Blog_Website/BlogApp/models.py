from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name = "Başlık")
    text = models.TextField(verbose_name="Yazı")
    created_date = models.DateTimeField(default=timezone.now, verbose_name = "Tarih")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = "Yazar")
    image = models.ImageField(upload_to="media", verbose_name="Resim")

    def __str__(self) -> str:
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=30, verbose_name="İsim")
    image = models.ImageField(upload_to="media", verbose_name="Resim")
    text = models.TextField(verbose_name="Hakkımda", max_length=200)

    def __str__(self) -> str:
        return self.name

class SocialMedia(models.Model):
    pass
