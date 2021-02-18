from django.urls import path
from bims_app import views


# backend urls
urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('client/',views.clientview,name='client'),
    path('loan/',views.loansview,name='loan'),
    path('group/',views.groupview,name='group'),
    path('application/',views.applicationsview,name='application'),
    path('client/add/',views.addclientview,name='add-client'),
    path('client/update/<int:client_id>',views.updateclientview,name='update-client'),
    path('client/delete/<int:client_id>',views.deleteclientview,name='delete-client'),
    path('group/add/',views.addgroupview,name='add-group'),
    path('group/update/<int:group_id>',views.updategroupview,name='update-group'),
    path('group/delete/<int:group_id>',views.deletegroupview,name='delete-group'),
    path('loan/create/',views.createloansview,name='create-loan'),
    path('loan/update/<int:loan_id>',views.updateloansview,name='update-loan'),
    path('loan/delete/<int:loan_id>',views.deleteloansview,name='delete-loan'),


    # frontend
    path('',views.homepageview,name='home'),
    path('about/',views.aboutpageview,name='about'),
    # path('contact/',views.contactpageview,name='contact'),
]

