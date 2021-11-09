from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def fiveGroup(request):
    return HttpResponse('우리는 오로나민C조 입니다 ^-^')