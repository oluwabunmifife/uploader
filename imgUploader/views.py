from django.contrib import messages
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

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']

            new_image = Images.objects.create(file=file, name=name, description=description)
            new_image.save()
            return redirect("project:House")
    else:
        return render(request, 'fileupload.html',{'form': form})


def House(request):
    pic = Images.objects.all()
    return render(request, 'house.html', {'pic': pic})


def page(request, pk):
    pk = pk
    return render(request, 'page.html', {"pk":pk})