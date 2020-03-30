from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseForbidden
from .models import Level, Category, Word, Theme
from .serializers import LevelsSerializer, ThemesSerializer, WordsSerializer, CategorySerializer, ThemeSerializer
from app.settings import API_SECRET


def check_api_secret(view_func):
    def wrap(self, *args, **kwargs):
        header = self.request.headers.get('Secret', None)
        if header != API_SECRET:
            return HttpResponseForbidden()
        else:
            return view_func(self.request, *args, **kwargs)
    return wrap


class LevelsView(APIView):
    @check_api_secret
    def get(self, request):
        levels = Level.objects.all()
        serializer = LevelsSerializer(levels, many=True)
        return Response(serializer.data)


class CategoriesView(APIView):
    @check_api_secret
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class ThemesView(APIView):
    @check_api_secret
    def get(self, request):
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
    @check_api_secret
    def get(self, request, id):
        themes = Theme.objects.filter(id=id)
        serializer = ThemeSerializer(themes, many=True)
        return Response(serializer.data)


class WordsView(APIView):
    @check_api_secret
    def get(self, request, id):
        words = Word.objects.filter(id=id)
        serializer = WordsSerializer(words, many=True)

        return Response(serializer.data)
