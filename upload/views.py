from django.contrib.auth import mixins
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView

from upload.decorator import check_user
from upload.forms import UserUploadForm
from upload.models import Upload
from accounts.models import User, Standard


# def main(request):
#     return render(request, 'upload/main.html')
#
#
# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
user_required = [login_required, check_user]


@method_decorator(login_required, 'post')
class UploadView(CreateView):
    model = Upload
    form_class = UserUploadForm
    template_name = 'upload/main.html'

    def form_valid(self, form):
        temp_upload = form.save(commit=False)
        temp_upload.user = self.request.user
        print(temp_upload.user.n_code)
        #yolo 함수 추가
        temp_upload.save()
        return super().form_valid(form)

    def get_success_url(self):
        print(self.object.pk, self.object.user)
        return reverse('upload:detail',kwargs={'pk':self.object.pk})
        #이미지 및 class_list (음식명) return 추가

@method_decorator(check_user, 'get')
class UploadDetailView(DetailView):
    model = Upload
    context_object_name = 'upload_result'
    template_name = 'upload/detail.html'