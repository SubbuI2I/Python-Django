from . import views
from django.urls import path

urlpatterns = [
    path('meetups/', views.index), #our-domin.com/meetups/
    path('', views.index), #our-domin.com/meetups/
    path('meetup-detail/<slug:meetup_slug>', views.meetup_details, name='meetup-details')
]