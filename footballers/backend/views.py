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
    return HttpResponse("This is the API index.")


def list_footballers(request):
    """
    Returns footballers list in JSON
    https://docs.djangoproject.com/en/1.11/topics/serialization/
    """
    data = serializers.serialize('json', Footballer.objects.all())
    resp = {'footballers': json.loads(data)}
    # not sure about json.loads here
    return JsonResponse(resp)


def get_footballer(request, player_id):
    """
    Get single player
    """
    data = serializers.serialize('json', [Footballer.objects.get(pk=player_id)])
    resp = json.loads(data)[0]
    return JsonResponse(resp)
