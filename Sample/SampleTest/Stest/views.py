from django.shortcuts import render
from django.http import HttpResponse

def Stest(request):
    return HttpResponse('Welcome to out test sample')


def Stest(request):
    return HttpResponse('Our'+ str(pk) + 'Stest')

# Create your views here
Stestlist = [
    {
        'Hello':'World'
    },
    {
        'Hey':'Sup'
    },
]