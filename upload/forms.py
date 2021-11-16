from django.forms import ModelForm
from upload.models import Upload


class UserUploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ['image', 'mealtimes']