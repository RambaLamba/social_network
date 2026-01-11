from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/',
                               blank=True,
                               null=True,
                               verbose_name='Аватар')
    age = models.IntegerField(null=True, verbose_name='Возраст')
    MARITAL_STATUS = [('Женат/замужем', 'Женат/замужем'),
                      ('Не женат/Не замужем', 'Не женат/Не замужем'),
                      ('В разводе', 'В разводе'),
                      ('Вдовец/Вдова', 'Вдовец/Вдова'),
                      ('Помолвлен/помолвлена', 'Помолвлен/помолвлена')]
    family_status = models.CharField(choices=MARITAL_STATUS,
                                     blank=True,
                                     default='',
                                     verbose_name='Семейное положение')
    bio = models.CharField(max_length=512, blank=True, verbose_name='Описание профиля')


class Image(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/%Y/%m/%d/',
                              verbose_name='Изображения',
                              blank=True,
                              null=True)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=2048, blank=True)

    def __str__(self):
        return f"Image {self.title} - {self.profile.user.username}"


class Publication(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='publications')
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='posts/%Y/%m/%d/',
                              verbose_name='Изображения',
                              blank=True,
                              null=True)
    
    def __str__(self):
        return self.title