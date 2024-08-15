from django.contrib import admin
from django.urls import path
from api.views import analyze, general_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analyze-text/', analyze, name="analyze_text"),
    path('general-search/', general_search, name="general_search"),
]
