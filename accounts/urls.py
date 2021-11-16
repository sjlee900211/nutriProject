
from django.urls import path, include

from accounts.views import SignUpView, LoginView, log_out, UserMyPageView, UserUpdateView

#해당 네임에서 url patterns에 있는 name의 url로 가주세요~!
app_name = "accounts"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),

    path('mypage/<int:pk>', UserMyPageView.as_view(), name='detail'),
    path('update/<int:pk>', UserUpdateView.as_view(), name="update"),
]

