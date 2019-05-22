from django.http import HttpResponse
from django.shortcuts import render


def chart_list(request):
    return HttpResponse(
        '<h1>인덱스 페이지<h1>'
        '또는'
        '<h2>벅스뮤직 차트 리스트 페이지<h2>')
