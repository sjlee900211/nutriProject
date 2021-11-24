from .views import dash
from django.urls import path, include


#해당 네임에서 url patterns에 있는 name의 url로 가주세요~!
app_name = "dashes"

urlpatterns = [
    path('dash/', dash, name='dash'),
]
