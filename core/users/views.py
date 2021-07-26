from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def view_user(request):
    return HttpResponse("hey threre i finally deployed the whole thing in elastic bean stalk ")
