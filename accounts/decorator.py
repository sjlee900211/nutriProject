from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

from accounts.models import User


def required(func):
    def decorated(request,*args,**kwargs):
        print(request.user)
        user = User.objects.get(pk=kwargs['pk'])
        print(kwargs['pk'])
        if not user == request.user:
            messages.info(request, "You can't go!")
            return redirect('accounts:main')
        return func(request,*args,**kwargs)
    return decorated

