from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("just test",status=200)