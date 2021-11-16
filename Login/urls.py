from django.urls import path
from . import views

app_name = "Login"
urlpatterns = [
    path('', views.User_list, name="list"),
    path('signup', views.createsignup, name="signup"),
    path('<id>', views.profile, name="profile"),
    path('<id>/edit', views.edit, name="edit"),
]

