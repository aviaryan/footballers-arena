# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from .models import Footballer


def index(request):
    """
    Root handler:
    https://docs.djangoproject.com/en/1.11/intro/tutorial01/
    """
    return HttpResponse("Hello, world. You're at the backend index.")


def list_footballers(request):
    """
    Returns footballers list in JSON
    https://docs.djangoproject.com/en/1.11/topics/serialization/
    """
    data = serializers.serialize("json", Footballer.objects.all())
    resp = {'footballers': json.loads(data)}
    # not sure about json.loads here
    return JsonResponse(resp)
