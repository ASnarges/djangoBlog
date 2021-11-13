from django.urls import path
from . import views

app_name= 'accounts'
urlpatterns =[
    path('signup', views.signup_view, name='signup'),
    path('login2', views.login2_view, name='login2'),
    path('logout', views.logout_view, name='logout'),

]