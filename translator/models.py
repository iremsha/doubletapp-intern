from django.db import models
from django.db.models import Model, CharField, IntegerField, AutoField


def upload_to(instance, filename):
    return 'media/{}'.format(filename)


class Category(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=155)
    icon = models.ImageField(verbose_name='Icon link', upload_to=upload_to, blank=True)

    def __str__(self):
        return self.name


class Level(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=155)
    code = CharField(max_length=155)

    def __str__(self):
        return self.code


class Word(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=155)
    translation = CharField(max_length=155)
    transcription = CharField(max_length=155)
    example = CharField(max_length=155)
    sound = models.ImageField(verbose_name='Sound link', upload_to=upload_to, blank=True)

    def __str__(self):
        return self.name


class Theme(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=155)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, default=1)
    words = models.ManyToManyField(Word)
    photo = models.ImageField(verbose_name='Photo link', upload_to=upload_to, blank=True)

    def __str__(self):
        return self.name
