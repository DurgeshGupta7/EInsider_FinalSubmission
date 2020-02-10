from django.urls import path
#imported views from the same app
from . import views

urlpatterns = [
    path('note/', views.home, name="home"),
    path ('note/delete/<list_id>/', views.delete, name="delete"),
    path ('note/cross_off/<list_id>/', views.cross_off, name="cross_off"),
	path ('note/uncross/<list_id>/', views.uncross, name="uncross"),
    path ('note/edit/<list_id>/', views.edit, name="edit"),
]