from django.urls import path
from . import views

urlpatterns = [
    path("/", views.home, name="bca.home"),

    # BCA 2080
    path("/bca80", views.bca80, name="bca80"),
    path("/formbca80", views.formbca80, name="formbca80"),
    path("/formbca80/editbca80/<pk>", views.editbca80, name="editbca80"),
    path("/formbca80/delbca80/<pk>", views.delbca80, name="delbca80"),

    # BCA 2079
    path("/bca79", views.bca79, name="bca79"),
    path("/formbca79", views.formbca79, name="formbca79"),
    path("/formbca79/editbca79/<pk>", views.editbca79, name="editbca79"),
    path("/formbca79/delbca79/<pk>", views.delbca79, name="delbca79"),

    # BCA 2078
    path("/bca78", views.bca78, name="bca78"),
    path("/formbca78", views.formbca78, name="formbca78"),
    path("/formbca78/editbca78/<pk>", views.editbca78, name="editbca78"),
    path("/formbca78/delbca78/<pk>", views.delbca78, name="delbca78"),

    # BCA 2077
    path("/bca77", views.bca77, name="bca77"),
    path("/formbca77", views.formbca77, name="formbca77"),
    path("/formbca77/editbca77/<pk>", views.editbca77, name="editbca77"),
    path("/formbca77/delbca77/<pk>", views.delbca77, name="delbca77"),

]
