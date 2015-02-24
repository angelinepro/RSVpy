from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import TemplateSettingsView


urlpatterns = patterns('',
    url(r'^$', TemplateSettingsView.as_view(template_name='index.html')),
    url(r'^contact/?$', TemplateSettingsView.as_view(template_name='contact.html')),
    url(r'^r/', include('invites.urls', namespace='invites')),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
