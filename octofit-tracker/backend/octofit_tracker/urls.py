from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
import os

# API root view that returns the Codespace URL dynamically

def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    api_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    return JsonResponse({"api_root": api_url})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
]
