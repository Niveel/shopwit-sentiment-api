from django.shortcuts import render
from .sentiment import analyze_sentiment
from .search import google_shopping_shop_search

from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.


@api_view(["GET"])
def analyze(request):
    message_content = request.GET.get("message")
    return Response({"message": analyze_sentiment(message_content)})


@api_view(["GET"])
def general_search(request):
    api_key = 'd1bded552ea0e5d1a5c04c5794ad879e1ee3f5c3dff4626ac15de1b02c37e1c6'
    query = request.GET.get("query")
    products = google_shopping_shop_search(api_key, query)
    return Response(products)