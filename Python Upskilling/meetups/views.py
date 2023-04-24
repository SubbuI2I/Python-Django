from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
  meetups = [
      {'title': '1st Meetup', 'location': 'New York', 'slug': 'a-first-meetup'},
      {'title': '2nd Meetup', 'location': 'Chennai', 'slug': 'a-second-meetup'},
      {'title': '3rd Meetup', 'location': 'Karaikudi', 'slug': 'a-third-meetup'},
  ]
  return render(request,'meetups/index.html',{
    'show_meetups': True,
    'meetups': meetups
  })

def meetup_details(request, meetup_slug):
    selected_meetup = {
       'title': '1st Meetup', 'location': 'New York', 'slug': 'a-first-meetup'
    }

    return render(request, 'meetups/meetup-detail.html', {
       'meetup_detail': selected_meetup
    })