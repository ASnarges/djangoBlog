from django.urls import path
from . import views

app_name = "Login"
urlpatterns = [
    path('', views.Login_list, name="list"),
    path('<slug>', views.Login_detail, name= "detail"),

]