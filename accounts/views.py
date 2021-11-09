from django.shortcuts import render

# Create your views here.

def upload(request):
    form = UploadForm()
    return render(request, 'kilogram/upload.html', {'form', form})