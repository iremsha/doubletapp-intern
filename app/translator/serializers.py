from rest_framework import serializers
from .models import Category, Theme, Level, Word


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'icon')


class LevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'name', 'code')


class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'name', 'translation', 'transcription', 'example', 'sound')


class ThemesWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'name')


class ThemesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'category', 'level', 'name', 'photo')


class ThemeSerializer(serializers.ModelSerializer):
    words = ThemesWordsSerializer(many=True)

    class Meta:
        model = Theme
        fields = ('id', 'category', 'level', 'name', 'photo', 'words')
