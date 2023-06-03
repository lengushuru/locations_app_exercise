from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('location_record/<int:pk>/', views.location_record, name='location_record'),
    path('delete_record/<int:pk>/', views.delete_record, name='delete_record'),
    path('delete_child/<int:pk>', views.delete_child, name='delete_child'),
    path('add_record/', views.add_record, name='add_record'),
    path('add_record_parent/', views.add_record_parent, name='add_record_parent'),
]
