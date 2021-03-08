import os

from django.utils.safestring import mark_safe

from app.settings import MEDIA_ROOT


def get_picture_widget(data):
    if not data:
        return 'https://lh4.ggpht.com/SptxaMS8ZkJNuCKXXO6GCep17pb8R8B6mVhGC4xmf2-v9SIeHRms9TEOvhCvQ-z66A_T=w300-rw'
    return data


def get_audio_widget(data):
    if not data:
        return 'https://psv4.vkuseraudio.net/c613129/u302770787/audios/53f05e25018a.mp3'
    return data


def widget_tag(field, type_widget):
    if type_widget == 'icon':
        return mark_safe('<img src="{}" width="50" height="50"/>'.format(get_picture_widget(field.icon)))
    elif type_widget == 'photo':
        return mark_safe('<img src="{}" width="100" height="100"/>'.format(get_picture_widget(field.photo)))
    else:
        return mark_safe('<audio controls><source src="{}" type="audio/mpeg"></audio>'.format(get_audio_widget(field.sound)))
