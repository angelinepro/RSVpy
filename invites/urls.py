from django.conf.urls import patterns, url
from invites import views

urlpatterns = patterns('',
    # ex: /invites/
    url(r'^$', views.index, name='index'),
    # ex: /invites/5/
    url(r'^(?P<party_ID>\d+)/$', views.detail, name='detail'),
    # ex: /invites/5/results/
    url(r'^(?P<party_ID>\d+)/results/$', views.results, name='results'),
    # ex: /invites/5/vote/
    url(r'^(?P<party_ID>\d+)/vote/$', views.vote, name='vote'),
)   