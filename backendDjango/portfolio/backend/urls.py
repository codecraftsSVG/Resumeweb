from django.urls import path
from .views import VisitorView
from .views import visitor_list

app_name = 'backend'
urlpatterns = [
    path('visitors/', visitor_list, name='visitor_list'),
    path('', VisitorView.as_view(), name='visitor_api'),
    # Add more URLs as needed
]
