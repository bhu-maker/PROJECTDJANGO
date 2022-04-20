from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [path('list',views.listing),
               path('place',views.placenew),
               path('rest',views.restnew),
               path('wait',views.waitnew),
               path('listall',views.listingall),
               path('disp',views.display),
               path('prodisp',views.projectdisplay),
               path('irctc/<int:pk>',views.irctc),
               path('irctcname',views.irctcname)]
