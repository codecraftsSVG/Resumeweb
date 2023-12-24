# backend/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Visitor
# backend/views.py

from django.shortcuts import render

def visitor_list(request):
    return render(request, 'visitor_list.html')

@method_decorator(csrf_exempt, name='dispatch')
class VisitorView(View):
    def get(self, request, *args, **kwargs):
        visitors = Visitor.objects.all()
        data = [{'name': visitor.name, 'email': visitor.email} for visitor in visitors]
        return JsonResponse({'visitors': data})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        visitor = Visitor.objects.create(
            name=data.get('name', ''),
            email=data.get('email', '')
            # Add more fields as needed
        )
        return JsonResponse({'message': 'Visitor added successfully'})
