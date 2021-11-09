from django.urls import path, include

from accounts.views import main

#해당 네임에서 url patterns에 있는 name의 url로 가주세요~!
app_name = "accountsapp"

urlpatterns = [
    path('', main, name='main'),
]