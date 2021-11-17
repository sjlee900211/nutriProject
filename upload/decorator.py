from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

from accounts.models import User
from upload.models import Upload


# def check_user(func):
#     def decorated(request,*args,**kwargs):
#         print(request.user, *args, upload)
#         if request.user is None:
#             messages.info(request, "Please Login")
#             return redirect('accounts:login')
#
#         return func(request,*args,**kwargs)
#     return decorated

def check_user(func):
    def decorated(request,*args,**kwargs):
        upload = Upload.objects.get(pk=kwargs['pk'])
        if request.user.pk == None:
            messages.info(request, "Please Login!")
            return redirect('accounts:login')

        elif request.user.pk != upload.user.pk:
            messages.info(request, "You can't see T.T")
            return redirect('upload:main')

        return func(request, *args, **kwargs)
        # elif upload.user.get_username() != request.user.user_id:
        #     messages.info(request, "You can't see T.T")
    return decorated