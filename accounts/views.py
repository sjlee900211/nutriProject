
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DetailView, UpdateView
from . import forms
from .models import User


def main(request):
    return render(request, 'accounts/main.html')

class LoginView(FormView):

    template_name = "accounts/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("accounts:main")

    def form_valid(self, form):
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, user_id=user_id, password=password)
        name = User.objects.get(user_id=user_id)
        username = name.name
        messages.info(self.request, "Welcome!")
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def log_out(request):
    messages.info(request, "See you later")
    logout(request)
    return redirect('accounts:login')

class SignUpView(FormView):
    template_name = "accounts/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("accounts:main")

    def form_valid(self, form):
        temp_user = form.save(commit=False)
        # temp_user.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()
        # temp_user.n_code = Standard.objects.get(gender=self.request.POST['gender'] , age_category=self.request.POST['age_category'])
        weight = self.request.POST['weight']
        height = self.request.POST['height']
        activity = self.request.POST['activity']
        if self.request.POST['gender'] == 1:
            temp_user.proper_cal = round((66.47 + (13.75 * float(weight)) + (5 * float(height)) - (6.76 * 30))*float(activity))
        else:
            temp_user.proper_cal = round((655.1 + (9.56 * float(weight)) + (1.85 * float(height)) - (4.68 * 30))*float(activity))
        temp_user.save()
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        temp_user.password = make_password(password)
        temp_user.save()
        user = authenticate(user_id=user_id, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class UserMyPageView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accounts/detail.html'


class UserUpdateView(UpdateView):
    model = User
    template_name = 'accounts/update.html'
    context_object_name = 'target_user'
    form_class = forms.UserUpdateForm


    def form_valid(self, form):
        temp_user = form.save(commit=False)
        # temp_user.n_code = Standard.objects.get(gender=self.request.POST['gender'] , age_category=self.request.POST['age_category'])
        weight = self.request.POST['weight']
        height = self.request.POST['height']
        activity = self.request.POST['activity']
        if self.request.POST['gender'] == 1:
            temp_user.proper_cal = round((66.47 + (13.75 * float(weight)) + (5 * float(height)) - (6.76 * 30))*float(activity))
        else:
            temp_user.proper_cal = round((655.1 + (9.56 * float(weight)) + (1.85 * float(height)) - (4.68 * 30))*float(activity))
        temp_user.save()
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        temp_user.password = make_password(password)
        temp_user.save()
        user = authenticate(user_id=user_id, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        messages.info(self.request, "Sucess!")
        return reverse('accounts:detail', kwargs={'pk': self.object.pk})
    # def post(self,request):
    #     if request.method == "POST":
    #         parent_name = request.POST.get('post')
    #         #parent_name = user
    #         node_parent = None
    #     if parent_name is not None:
    #         node_parent = Node.objects.get(name=parent_name)

    #     Node.objects.create(parent=node_parent)
    # def form_valid(self, form):
    #     # age_category = form.data.get('age_category')
    #     # weight = form.data.get('weight')
    #     # height = form.data.get('weight')
    #     # code = Standard.objects.get(age_category=age_category)
    #     # print(code)
    #     # user = User (
    #     #     n_code=code,
    #     #     proper_cal=float(66.47 + (13.75 * float(weight)) + (5 * float(height)) - (6.76 * 30)),
    #     # )
    #     # # print(user)
    #     # user.save()
    #     print(form)
    #     form.save()
    #     user_id = form.cleaned_data.get('user_id')
    #     password = form.cleaned_data.get('password')
    #     user = authenticate(self.request, user_id=user_id, password=password)
    #     if user is not None:
    #         login(self.request, user)
    #     return super().form_valid(form)
    # def post(self, request):
    #     user_data = json.loads(request.body)
    #     try:
    #
    #         with transaction.atomic():
    #             password = bcrypt.hashpw(user_data['password'].encode('utf-8'), bcrypt.gensalt())
    #
    #             user_model = User(
    #                 account=user_data['account'],
    #                 grade=Grade.objects.get(id=1),
    #                 password=password.decode(),
    #                 name=user_data['name'],
    #                 email=user_data['email'],
    #                 phone=user_data['phone'],
    #                 gender=Gender.objects.get(name=user_data['gender']),
    #                 birthday=user_data['birthday']
    #             )
    #
    #             user_model.save()
    #
    #             # capital area check
    #             Address(
    #                 user=User.objects.get(id=user_model.id),
    #                 address=user_data['address'],
    #                 is_capital_area=self.check_capital_area(user_data['address'])
    #             ).save()
    #
    #             return HttpResponse(status=200)
    #
    #     except KeyError:
    #         return HttpResponse(status=400)
    #
    #     except ValidationError:
    #         return HttpResponse(status=400)



    # if request.method == "POST":
    #     temp = request.POST.get('n_code')
    #     print(temp)
    #     try:
    #         data = json.loads(request.body)
    #         user_id = data['user_id']
    #         password = data['password']
    #         name = data['name']
    #         height = data['height']
    #         weight = data['weight']
    #         age_category = data['age_category']
    #         gender = data['gender']
    #         activity = data['activity']
    #
    #         user = User.objects.create(
    #             user_id=user_id,
    #             password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode(),  # hash이후 바로 decode,
    #             name=name,
    #             height=height,
    #             weight=weight,
    #             age_category=age_category,
    #             activity=activity,
    #             gender=gender,
    #             codename=Standard.objects.n_code.filter(Q(gender=gender)),
    #             proper_cal=66.47 + (13.75 * weight) + (5 * height) - (6.76 * 30),
    # #         )
    #         print(user)
    #         return JsonResponse({'MESSAGE': 'SUCCESS TO MAKE ACCOUNT'}, status=201)
    #
    #
    #     except:
    #         return render(request, 'accounts/main.html')


# def add_info(request):
#     if request.method == "POST":
#         temp = request.POST.get("n_code")
#         n_code = Standard.all().filter(Q)

