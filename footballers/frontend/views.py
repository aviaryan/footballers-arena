# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    """
    home page
    https://docs.djangoproject.com/en/1.11/intro/tutorial03/
    """
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))
