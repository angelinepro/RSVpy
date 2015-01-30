from django.conf.urls import patterns, url
from invites import views

urlpatterns = patterns('',
    # ex: /invites/
    url(r'^$', views.index, name='index'),
    # ex: /invites/5/
    url(r'^(?P<party_ID>\d+)/(?P<token>[A-Z0-9]+)$', views.detail, name='detail'),
    # ex: /invites/5/results/
    url(r'^(?P<party_ID>\d+)/(?P<token>[A-Z0-9]+)/results/$', views.results, name='results'),
    # ex: /invites/5/vote/
    url(r'^(?P<party_ID>\d+)/(?P<token>[A-Z0-9]+)/vote/$', views.vote, name='vote'),
)   