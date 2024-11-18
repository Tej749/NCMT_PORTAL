from django.urls import path
from . import views_csit

urlpatterns = [
    path("/", views_csit.home, name="csit.home"),

    # batch csit 2080
    path("/csit80", views_csit.csit80, name="csit80"),
    path("/formcsit80", views_csit.formcsit80, name="formcsit80"),
    path("/formcsit80/editcsit80/<pk>", views_csit.editcsit80, name="editcsit80"),
    path("/formcsit80/delcsit80/<pk>", views_csit.delcsit80, name="delcsit80"),

    # batch csit 2079
    path("/csit79", views_csit.csit79, name="csit79"),
    path("/formcsit79", views_csit.formcsit79, name="formcsit79"),
    path("/formcsit79/editcsit79/<pk>", views_csit.editcsit79, name="editcsit79"),
    path("/formcsit79/delcsit79/<pk>", views_csit.delcsit79, name="delcsit79"),

    # batch csit 2078
    path("/csit78", views_csit.csit78, name="csit78"),
    path("/formcsit78", views_csit.formcsit78, name="formcsit78"),
    path("/formcsit78/editcsit78/<pk>", views_csit.editcsit78, name="editcsit78"),
    path("/formcsit78/delcsit78/<pk>", views_csit.delcsit78, name="delcsit78"),

    # batch csit 2077
    path("/csit77", views_csit.csit77, name="csit77"),
    path("/formcsit77", views_csit.formcsit77, name="formcsit77"),
    path("/formcsit77/editcsit77/<pk>", views_csit.editcsit77, name="editcsit77"),
    path("/formcsit77/delcsit77/<pk>", views_csit.delcsit77, name="delcsit77"),
]
