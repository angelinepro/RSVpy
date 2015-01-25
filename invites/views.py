from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from django.shortcuts import get_object_or_404, render
from invites.models import Person
from invites.models import Party
from django.utils import timezone

def index(request):
    party_list = Party.objects.order_by('-Head')[:5]
    context = {'party_list': party_list}
    return render(request, 'invites/index.html', context)

#def index(request):
#    person_list = Person.objects.order_by('-Coming')[:5]
#    context = {'person_list': person_list}
#    return render(request, 'invites/index.html', context)

def detail(request, party_ID):
    party = get_object_or_404(Party, pk=party_ID)
    member_list = party.members.order_by('-name')
    head = party.head
    party.viewDate = timezone.now()
    party.save()
    context = {'member_list': member_list, 'head': head, 'party_ID': party_ID}
    return render(request, 'invites/detail.html', context)

 #   context = {'member_list': member_list}
 #   return render(request, 'invites/detail.html', context)
 #   party = get_object_or_404(Party, title='ID')

#    response = 'Here is the head of the Party: %s.'
#    return HttpResponse(response % party.Head)


#def detail(request, Name):
#    person = get_object_or_404(Person, pk=Name)
#    return render(request, 'invites/detail.html', {'person': person})

#    try:
#        person = Person.objects.get(pk=Name)
#    except Person.DoesNotExist:
#        raise Http404
#    return render(request, "invites/detail.html", {'person': person})

def results(request, party_ID):
    party = get_object_or_404(Party, pk=party_ID)
    response = "You're looking at the results of %s."
    return HttpResponse(response % party.head)

def vote(request, party_ID):
    party = get_object_or_404(Party, pk=party_ID)
    attendees = request.POST.getlist('member')
    for attendee in attendees:
        person_instance = get_object_or_404(Person, pk=attendee)
        person_instance.coming = True
        person_instance.save()    
    party.submitDate = timezone.now()
    party.save()
    return render(request, 'invites/vote.html')
