from django.http import HttpResponseForbidden
from app.settings import API_SECRET

from django.utils.deprecation import MiddlewareMixin


class CheckAPISecret(MiddlewareMixin):

    def process_request(self, request):
        if request.path[:5] == '/api/':
            header = request.headers.get('Secret', None)
            if header != API_SECRET:
                return HttpResponseForbidden()


