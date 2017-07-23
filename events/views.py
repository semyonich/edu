from django.shortcuts import render, HttpResponse

from accounts.models import User
from events.models import Event

def events_list(request):
    event = Event.objects.get(id=1)
    event.members.remove(User.objects.get(email='test@gmail.com'))
    event.save()
    # print(event.title)
    # event.title = 'new title'
    # event.save()
    # print(event.title)
    # print(event.date)
    # print(event.members.all())
    return HttpResponse('dfgdgdfgdfg')
