from django.shortcuts import render
from .sentiment import analyze_sentiment
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(["GET"])
def analyze(request):
    message_content = request.GET.get("message")
    return Response({"message": analyze_sentiment(message_content)})
