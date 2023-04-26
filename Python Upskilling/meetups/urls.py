from . import views
from django.urls import path

urlpatterns = [
    path('meetups/', views.index), #our-domin.com/meetups/
    path('', views.index), #our-domin.com/meetups/
    path('confirm-registration/<slug:meetup_slug>/success', views.registration_confirmation, name='confirm-registration'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-details'),
]