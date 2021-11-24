# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from .models import StatelessApp


# def add_stateless_apps(request, **kwargs):
#     """Check all registered stateless apps and create ORM entries that are missing"""
#     # check_stateless_loaded()
#     # dash_app = reverse_lazy("accounts:dash")
#     return redirect(reverse_lazy("dashes:dash"))

from django.shortcuts import render
from django.http import HttpResponse
from .models import Dash
from django.contrib import messages
from django.urls import reverse
    
# def dash(request):
#     model = Dash
#     template_name = 'dashes/dash.html'
#     return render(request, template_name)
# @method_decorator(required, 'get')
def dash(request):
    # messages.info(self.re, "Success!")
    # return reverse('dashes:dash', HttpResponse(resp))
    return render(request, 'dashes/dash.html')