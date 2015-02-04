from django.conf.urls import patterns, url
from invites import views
from invites.models import TOKEN_CHARSET


urlpatterns = patterns('',
    # ex: /r/ABCD123/
    url(r'^(?P<token>[%s]+)$' % TOKEN_CHARSET, views.rsvp, name='rsvp'),
)
