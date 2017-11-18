# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Root handler:
    https://docs.djangoproject.com/en/1.11/intro/tutorial01/
    """
    return HttpResponse("Hello, world. You're at the backend index.")
