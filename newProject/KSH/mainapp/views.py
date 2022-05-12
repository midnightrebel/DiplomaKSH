from django.shortcuts import render
from django.views import View
import json
# Create your views here.
from rest_framework import viewsets

from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer

class FrontendTemplateView(View):
    def post(self, request):
        # Собираем все параметры запроса в контекст
        context = {
            'post_data': request.body,
            'get_data': json.dumps(request.GET)  # Сериализуем в JSON
        }

        # Отправляем клиенту отрендеренный с контекстом шаблон
        return render(request, 'index.html', context)