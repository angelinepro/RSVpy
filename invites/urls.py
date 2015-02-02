from django.conf.urls import patterns, url
from invites import views
from invites.models import TOKEN_CHARSET


urlpatterns = patterns('',
    # ex: /invites/
    url(r'^$', views.index, name='index'),
    # ex: /invites/5/
    url(r'^(?P<token>[%s]+)$' % TOKEN_CHARSET, views.detail, name='detail'),
    # ex: /invites/5/rsvp/
    url(r'^(?P<token>[%s]+)/rsvp/$' % TOKEN_CHARSET, views.rsvp, name='rsvp'),
)
