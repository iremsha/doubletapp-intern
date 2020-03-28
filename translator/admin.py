from django.contrib import admin
from django.utils.safestring import mark_safe
from django.conf import settings

from .models import Category, Theme, Level, Word


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    fields = ['name', 'code']
    list_filter = ['code']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_tag')
    fields = ['icon_tag', 'name', 'icon']
    readonly_fields = ['icon_tag']

    def icon_tag(self, obj):
        return mark_safe(f'<img src="{ settings.MEDIA_URL }{ obj.icon }" width="50" height="50">')

    icon_tag.short_description = 'Icon'


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo_tag', 'category', 'level')
    list_filter = ['level', 'category']
    fields = ['photo_tag', 'name', 'category', 'level', 'photo', 'words']
    readonly_fields = ['photo_tag']

    def photo_tag(self, obj):
        return mark_safe(f'<img src="{ settings.MEDIA_URL }{ obj.photo }" width="100" height="100">')

    photo_tag.short_description = 'Photo'


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'sound_tag', 'translation', 'transcription', 'example')
    list_filter = ['name']
    fields = ['sound_tag', 'name', 'translation', 'transcription', 'example', 'sound']
    readonly_fields = ['sound_tag']

    def sound_tag(self, obj):
        return mark_safe(f'<audio controls><source src="{ settings.MEDIA_URL }{ obj.sound }" type="audio/ogg"></audio>')

    sound_tag.short_description = 'Sound'
