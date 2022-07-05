from django.shortcuts import render
from .forms import ImageForm

# Create your views here.
def imgUpload(request):
    form = ImageForm
    return render(request, 'fileupload.html',{'form': form})