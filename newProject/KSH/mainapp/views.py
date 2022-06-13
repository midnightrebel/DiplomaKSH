from django.shortcuts import render
from django.views import View
import json
# Create your views here.
from rest_framework import viewsets
from django.views.generic import TemplateView





class Index(TemplateView):
    template_name = "index.html"
    url = str(input("Ссылка на турнирную таблицу:"))
    if url.__contains__('contestscoreboard'):
        url = url.replace('contestscoreboard', 'contestscoreboardgrid')

class FrontendTemplateView(View):
    def post(self, request):
        # Собираем все параметры запроса в контекст
        context = {
            'post_data': request.body,
            'get_data': json.dumps(request.GET)  # Сериализуем в JSON
        }

        # Отправляем клиенту отрендеренный с контекстом шаблон
        return render(request, 'index.html', context)