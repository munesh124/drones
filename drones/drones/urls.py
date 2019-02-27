from django.conf.urls import url
from . import views


urlpatterns = [

    url('categories/$', views.DroneCategoryList.as_view(),name='dronecategory-list'),
    url('categories/(?P<pk>[0-9]+)/', views.DroneCategoryDetail.as_view(), name='dronecategory-detail'),
    url('drones/$', views.DroneList.as_view(), name='drone-list'),
    url('drones/(?P<pk>[0-9]+)/', views.DroneDetail.as_view(), name='drone-detail'),
    url('pilots/$', views.PilotList.as_view(), name='pilot-list'),
    url('pilots/(?P<pk>[0-9]+)/', views.PilotDetail.as_view(), name='pilot-detail'),
    url('competitions/$', views.CompetitionList.as_view(), name='competition-list'),
    url('competitions/(?P<pk>[0-9]+)/', views.CompetitionDetail.as_view(), name='competition-detail'),
    url('', views.ApiRoot.as_view(),name=views.ApiRoot.name),




]
