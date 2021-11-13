from django.urls import path
from . import views

app_name = "Login"
urlpatterns = [
    path('', views.Login_list, name="list"),
    path('create', views.create_article, name= "create"),
    path('<slug>', views.Login_detail, name= "detail"),

]