from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import json
from django.core import serializers

from meetups.forms import RegistrationForm
from .models import Meetup, Participant
# Create your views here.

def index(request):
  meetups = []
  # Dynamic data mapping
  meetups = Meetup.objects.all() 
  
  # # Hard coded data mapping
  # meetups = [
  #     {'title': '1st Meetup', 'location': 'New York', 'slug': 'a-first-meetup'},
  #     {'title': '2nd Meetup', 'location': 'Chennai', 'slug': 'a-second-meetup'},
  #     {'title': '3rd Meetup', 'location': 'Karaikudi', 'slug': 'a-third-meetup'},
  # ]
  
  return render(request,'meetups/index.html',{
    'show_meetups': True,
    'meetups': meetups
  })

  
def meetup_details(request, meetup_slug):
   # print(meetup_slug)    
    try:          
      # # Hard coded data mapping
      # selected_meetup = {
      #    'title': '1st Meetup', 'location': 'New York', 'slug': 'a-first-meetup'
      # }

      selected_meetup =  Meetup.objects.get(slug=meetup_slug)
      # output = serializers.serialize('json', selected_meetup)
      # print(output)
      # return HttpResponse(output)
      if request.method == "GET":
        registration_form = RegistrationForm()  
      else:
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
          #participant = registration_form.save() # using ModelForm
          print('method' + request.method)
          user_email = '' # registration_form.cleaned_data['email']          
          try:
            participant, was_created = Participant.objects.get_or_create(email=user_email)
          except Participant.DoesNotExist:
            participant = None      
          selected_meetup.email.add(participant)
          print(participant)
          print('save - ' + user_email )
          return redirect('confirm-registration',slug=meetup_slug)
      
      return render(request, 'meetups/meetup-detail.html', {
          'meetups_found': True,
          'meetup_detail': selected_meetup,
          'form': registration_form
        })           
    
    except Exception as ex:
       print(ex)
       return render(request, 'meetups/meetup-detail.html', {
          'meetups_found': False
    })
       
def registration_confirmation(request, meetup_slug):
  print('confirm')
  return HttpResponse('meetup_slug')
  # meetup = Meetup.objects.get(slug=meetup_slug)
  # return render(request, 'meetups/registration-confirmation.html', {
  #   'isSuccess': True,
  #   'organizeremail': 'meetup.organizeremail'
  # })