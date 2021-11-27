from .views import dash
from django.urls import path, include
from accounts.views import UserMyPageView

app_name = "dashes"

urlpatterns = [
    # path('dash/<int:pk>', dash, name='dash'),
    path('dash/', dash, name='dash'),
]
