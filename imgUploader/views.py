from email.mime import image
from django.shortcuts import render
from .forms import ImageForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Images

# Create your views here.
def imgUpload(request):
    form = ImageForm
    if request.method == 'POST':
        file = request.POST['file']
        name = request.POST['name']
        description = request.POST['description']
        form = ImageForm(request.POST)
        pic = Images.objects.create(file=file, name=name, description=description)
        pic.save()
        return render(request, 'house.html', {'pic': pic})
            #return HttpResponseRedirect('/fileupload.html?submitted=True')

    else:
        return render(request, 'fileupload.html',{'form': form})

def House(request):
    pic = Images.objects.all()
    return render(request, 'house.html', {'pic': pic})