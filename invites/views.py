from django.http import HttpResponse, HttpResponseBadRequest
from django.templatetags.static import static
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from invites.models import Person, SeenBrowser
from invites.models import Party
from django.utils import timezone
from django.conf import settings
from django.contrib import messages

import user_agents


BAD_TOKEN_TXT = 'Invalid token. Please make sure you have typed the URL correctly into your browser.'


def rsvp(request, token):
    if request.method == 'POST':
        return rsvp_post(request, token)
    else:
        return rsvp_get(request, token)


def rsvp_get(request, token, redirected_from_post=False):
    party = get_object_or_404(Party, token=token)
    if party.token != token:
        return HttpResponseForbidden(BAD_TOKEN_TXT)

    def template_format(coming):
        if coming:
            return '1'
        elif coming is None:
            return ''
        else:
            return '0'

    member_list = ((member, template_format(member.coming)) for member in party.members.order_by('pk'))
    head = party.head

    # We can be sure that the invite has been looked at
    party.viewDate = timezone.now()
    party.save()

    # Save the user's browser for metrics
    ua = request.META.get('HTTP_USER_AGENT', None)
    if ua:
        save_browser(ua)

    # If the RSVP has been viewed already, populate the current values.
    rsvps = {}
    if party.submitDate and not redirected_from_post:
        messages.add_message(request, messages.INFO,
                             "You've already RSVPed. You can still change your "
                             "RSVP below and submit it again until RSVPs close.")
        for member in party.members.all():
            rsvps[member.pk] = member.coming

    context = {
        'member_list': member_list,
        'head': head,
        'party': party,
        'rsvps': rsvps,
        'settings': settings,
    }
    return render(request, 'invites/detail.html', context)


def rsvp_post(request, token):
    party = get_object_or_404(Party, token=token)
    if party.token != token:
        return HttpResponseForbidden('Invalid token.')

    i = 1
    data = {}
    while True:
        member_key = 'member%d' % i
        value_key = 'value%d' % i
        member_exists = member_key in request.POST
        value_exists = value_key in request.POST
        if all((member_exists, value_exists)):
            value = request.POST[value_key]
            if value == '':
                # Unanswered field
                messages.add_message(request, messages.ERROR, 'Please respond for all members of your party.')
                return rsvp_get(request, token, redirected_from_post=True)
            data[request.POST[member_key]] = request.POST[value_key] == '1'
            i += 1
        elif any((member_exists, value_exists)):
            return HttpResponseBadRequest('Unpaired values')
        else:
            break

    for pk, coming in data.items():
        person_instance = get_object_or_404(Person, pk=pk)
        person_instance.coming = coming
        person_instance.save()

    party.submitDate = timezone.now()
    party.save()

    messages.add_message(request, messages.SUCCESS, 'Thank you for your response!')
    return rsvp_get(request, token, redirected_from_post=True)


def save_browser(browser):
    parsed = user_agents.parse(browser)
    obj, _ = SeenBrowser.objects.get_or_create(defaults={
        'browser': parsed.browser.family,
        'version': parsed.browser.version_string
    })
    obj.times += 1
    obj.save()


def tracking(request, token):
    party = get_object_or_404(Party, token=token)
    party.emailViewDate = timezone.now()
    party.save()
    return redirect(static('img/1x1.gif'))
