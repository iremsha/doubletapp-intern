from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseForbidden
from .models import Level, Category, Word, Theme
from .serializers import LevelsSerializer, ThemesSerializer, WordsSerializer, CategorySerializer, ThemeSerializer
from app.settings import API_SECRET


class LevelsView(APIView):
    def get(self, request):
        header = request.headers.get('Secret', None)
        if header != API_SECRET:
            return HttpResponseForbidden()
        levels = Level.objects.all()
        serializer = LevelsSerializer(levels, many=True)
        return Response(serializer.data)


class CategoriesView(APIView):
    def get(self, request):
        header = request.headers.get('Secret', None)
        if header != API_SECRET:
            return HttpResponseForbidden()
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class ThemesView(APIView):
    def get(self, request):
        header = request.headers.get('Secret', None)
        if header != API_SECRET:
            return HttpResponseForbidden()
        themes = Theme.objects.all()
        category = request.GET.get('category')
        level = request.GET.get('level')
        if category:
            themes = themes.filter(category=category)
        if level:
            themes = themes.filter(level=level)
        serializer = ThemesSerializer(themes, many=True)
        return Response(serializer.data)


class ThemesFilterView(APIView):
    def get(self, request, id):
        header = request.headers.get('Secret', None)
        if header != API_SECRET:
            return HttpResponseForbidden()
        themes = Theme.objects.filter(id=id)
        serializer = ThemeSerializer(themes, many=True)
        return Response(serializer.data)


class WordsView(APIView):
    def get(self, request, id):
        header = request.headers.get('Secret', None)
        if header != API_SECRET:
            return HttpResponseForbidden()
        words = Word.objects.filter(id=id)
        serializer = WordsSerializer(words, many=True)

        return Response(serializer.data)
