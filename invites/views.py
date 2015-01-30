from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from invites.models import Person
from invites.models import Party
from django.utils import timezone


def index(request):
    party_list = Party.objects.order_by('-Head')[:5]
    context = {'party_list': party_list}
    return render(request, 'invites/index.html', context)

def detail(request, party_ID, token):
    party = get_object_or_404(Party, pk=party_ID)
    if party.token != token:
        return HttpResponseForbidden('Invalid URL')
    member_list = party.members.order_by('pk')
    head = party.head
    party.viewDate = timezone.now()
    party.save()
    context = {'member_list': member_list, 'head': head, 'party': party}
    return render(request, 'invites/detail.html', context)

def results(request, party_ID, token):
    party = get_object_or_404(Party, pk=party_ID)
    if party.token != token:
        return HttpResponseForbidden('Invalid URL')
    response = "You're looking at the results of %s."
    return HttpResponse(response % party.head)

def vote(request, party_ID, token):
    party = get_object_or_404(Party, pk=party_ID)
    if party.token != token:
        return HttpResponseForbidden('Invalid URL')
    member_list = party.members.order_by('pk')
    party_pk_list = []
    for member in member_list:
        member_pk = member.pk
        party_pk_list.append(member_pk)
    i = 1
    while 'member'+str(i) in request.POST:
        if 'value'+str(i) in request.POST:
            i += 1
        else:
            return HttpResponse('Invalid Request, Please Select Attending or Not Attending for Each Person')
    i = 1
    while 'member'+str(i) in request.POST:
        pk_list_instance = int(request.POST['member'+str(i)])
        if pk_list_instance in party_pk_list:
            i += 1
        else:
           return HttpResponse('Invalid Request, You Can Only Reserve For One Party At a Time')
    i = 1
    pk_list = []
    value_list = []
    while 'member'+str(i) in request.POST:
        pk_list_instance = request.POST['member'+str(i)]
        value_list_instance = request.POST['value'+str(i)]
        pk_list.append(pk_list_instance)
        value_list.append(value_list_instance)
        person_instance = get_object_or_404(Person, pk=pk_list_instance)
        person_instance.coming = value_list_instance=='1'
        person_instance.save()
        i += 1
    party.submitDate = timezone.now()
    party.save()
    return render(request, 'invites/vote.html')