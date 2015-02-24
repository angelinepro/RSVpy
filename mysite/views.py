from django.conf import settings
from django.views.generic.base import TemplateView


class TemplateSettingsView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(TemplateSettingsView, self).get_context_data(**kwargs)
        context['settings'] = settings
        return context
