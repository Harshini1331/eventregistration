from django.shortcuts import render
from .models import Participant
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    context = {}
    return render(request, 'eventapplication/home.html', context)

def register(request):
    context = {}
    if request.method == 'POST':
        p1 = Participant()
        p1.name = request.POST.get('name','-')
        p1.email = request.POST.get('email','-')
        p1.phonenumber = request.POST.get('phonenumber','000')
        p1.schoolname = request.POST.get('schoolname','-')

        if len(Participant.objects.all()) > 10:
            return render(request, 'eventapplication/failure.html', context)
        else:
            p1.save()
            return render(request, 'eventapplication/success.html', context)

    if request.method == 'GET':
        context['name'] = ''
        context['email'] = ''
        context['phonenumber'] = ''
        context['schoolname'] = ''

    return render(request, 'eventapplication/register.html', context)

def listofparticipants(request):
    context = {}

    context['participants'] = Participant.objects.all()
    
    return render(request, 'eventapplication/listofparticipants.html', context)

def success(request):
    context = {}
    return render(request, 'eventapplication/success.html', context)

def failure(request):
    context = {}
    return render(request, 'eventapplication/failure.html', context)