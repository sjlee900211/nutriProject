from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView

from upload.forms import UserUploadForm
from upload.models import Upload


# def main(request):
#     return render(request, 'upload/main.html')
#
#
# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
class UploadView(CreateView):
    model = Upload
    form_class = UserUploadForm
    template_name = 'upload/main.html'

    def form_valid(self, form):
        temp_upload = form.save(commit=False)
        temp_upload.user = self.request.user
        temp_upload.n_code = self.request.user.n_code
        temp_upload.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('upload:detail',kwargs={'pk':self.object.pk})

class UploadDetailView(DetailView):
    model = Upload
    context_object_name = 'target_upload'
    template_name = 'upload/detail.html'