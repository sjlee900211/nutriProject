from django.urls import path, include

from accounts.views import main, SignUpView

#해당 네임에서 url patterns에 있는 name의 url로 가주세요~!
app_name = "accounts"

urlpatterns = [
    path('', main, name='main'),
    # path('/login', main, name='login'),
    # path('/logout', main, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]

