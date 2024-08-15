from django.contrib import admin
from django.urls import path
from api.views import analyze, general_search, search_shop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analyze-text/', analyze, name="analyze_text"),
    path('general-search/', general_search, name="general_search"),
    path('search-shop/', search_shop, name="search_shop"),
]
