from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Dash
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def dash(request):
    return render(request, 'dashes/dash.html')

