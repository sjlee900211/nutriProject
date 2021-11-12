from django import forms
from . import models
from .models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("user_id",
                  "password",
                  "password_check",
                  "name",
                  "height",
                  "weight",
                  "age_category",
                  "gender",
                  "activity")
        widgets = {
            "user_id": forms.TextInput(attrs={"placeholder": "ID"}),
            "name": forms.TextInput(attrs={"placeholder": "이름"}),
            "height": forms.TextInput(attrs={"placeholder": "cm"}),
            "weight": forms.TextInput(attrs={"placeholder": "kg"})
        }

    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password_check = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password confirm"}))

    def clean(self):  # 요청파라미터 값들 조회
        cleaned_data = super().clean() # dictionary 반환.
        password = cleaned_data.get('password')
        password_check = cleaned_data.get('password_check') #password와 password_check 같은지 체크
        if password != password_check:
            self.add_error('password', '비밀번호가 일치하지 않습니다.')
            self.add_error('password_check', '비밀번호가 일치하지 않습니다.') # 이메일(아이디) 중복 체크

