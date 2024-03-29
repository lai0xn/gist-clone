from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_page,name="home"),
    path("gists/<int:pk>",views.gist_view,name="gist"),
    path("gists/create",views.CreateGist.as_view(),name="gist-create"),

]
