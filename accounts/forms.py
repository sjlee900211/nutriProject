from django import forms
from . import models

class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("user_id", "password","password_check", "name", "height","weight","age_category","gender","activity")
        widgets = {
            "user_id": forms.TextInput(attrs={"placeholder": "ID"}),
            "name": forms.TextInput(attrs={"placeholder": "이름"}),
            "height": forms.TextInput(attrs={"placeholder": "cm"}),
            "weight": forms.TextInput(attrs={"placeholder": "kg"})
        }

    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password_check = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password confirm"}))
    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password_check")

        if password != password1:
            raise forms.ValidationError("Password Confirmation does not match")

        else:
            return password