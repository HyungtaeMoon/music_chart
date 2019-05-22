from django.http import HttpResponse
from django.shortcuts import render


def login_view(request):
    return HttpResponse('<h1>members:login 페이지<h1>')
