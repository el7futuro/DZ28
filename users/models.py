from django.db import models


class User(models.Model):
    ROLE = [
        ("member", "пользователь"),
        ("admin", "администратор"),
        ("moderator", "модератор")
    ]
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=9, choices=ROLE, default="member")
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField('Location')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username


class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


