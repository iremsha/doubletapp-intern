from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Level, Category, Word
from .serializers import *
from rest_framework import generics


class LevelsView(APIView):
    def get(self, request):
        levels = Level.objects.all()
        serializer = LevelsSerializer(levels, many=True)
        return Response(serializer.data)


class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class ThemesView(APIView):
    def get(self, request):
        themes = Theme.objects.all()
        serializer = ThemesSerializer(themes, many=True)
        return Response(serializer.data)


class ThemesFilterView(APIView):
    def get(self, request, category, level):
        themes = Theme.objects.filter(category=category, level=level)
        serializer = ThemesSerializer(themes, many=True)
        return Response(serializer.data)


class WordsView(APIView):
    def get(self, request, id):
        words = Word.objects.filter(id=id)
        serializer = WordsSerializer(words, many=True)

        return Response(serializer.data)
