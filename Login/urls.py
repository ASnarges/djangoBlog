from django.urls import path
from . import views

app_name = "Login"
urlpatterns = [
    path('', views.User_list, name="list"),
    path('create', views.create_article, name= "create"),
    path('signup', views.createsignup, name="signup"),
    path('<name>', views.profile, name="profile"),
    #path('<slug>', views.Login_detail, name= "detail"),

]

