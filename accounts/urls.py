
from django.urls import path, include

from accounts.views import main, SignUpView, LoginView, log_out

#해당 네임에서 url patterns에 있는 name의 url로 가주세요~!
app_name = "accounts"

urlpatterns = [
    path('', main, name='main'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]

