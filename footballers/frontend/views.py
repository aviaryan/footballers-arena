from django.shortcuts import render


def index(request):
    """
    home page
    https://docs.djangoproject.com/en/1.11/intro/tutorial03/
    """
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})
