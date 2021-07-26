from django.urls import path , include
from .views import view_user


urlpatterns = [
    path('users', view_user ,name="user-view"),

]