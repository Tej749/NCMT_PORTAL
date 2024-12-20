from django.urls import path
from . import views

urlpatterns = [
    path("/main", views.main, name="main"),
    path("/signup", views.signup, name="signup"),
    path("/org.home", views.home, name="org.home"),
    path("/staff", views.staff, name="staff"),
    path("/form", views.form, name="form"),
    path("/form/edit/<pk>", views.edit, name="edit"),
    path("/form/delstaff/<pk>", views.delstaff, name="delstaff"),

]
