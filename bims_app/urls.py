from django.urls import path
from bims_app import views


# backend urls
urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('client/',views.clientview,name='client'),
    path('business/',views.businessview,name='business'),
    path('loans/',views.loansview,name='loans'),
    path('group/',views.groupview,name='group'),
    path('client/add/',views.addclientview,name='add-client'),
]