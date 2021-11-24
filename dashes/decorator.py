from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

from dashes.models import Dash


def check_user(func):
    def decorated(request,*args,**kwargs):
        print(request.user, *args, Dash)
        if request.user is None:
            messages.info(request, "Please Login")
            return redirect('accounts:login')

        return func(request,*args,**kwargs)
    return decorated
