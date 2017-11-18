from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^players$', views.list_footballers, name='list_footballers'),
    url(r'^players/(?P<player_id>[0-9]+)$', views.get_footballer, name='get_footballer')
]
