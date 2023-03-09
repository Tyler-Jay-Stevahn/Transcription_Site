from django.shortcuts import render, redirect
from .models import employees, registrationdata 
from .forms import registration_forms , FileUploadForm #, UploadFileForm
from .functions import to_dataframe
from .functions import transcriber
import os

# Create your views here.

def landingpage(request):
    context = {
        "greeting":"heylo"
    }
    return render(request, 'landingpage.html', context)

def home(request):
    context= {
        "name":"Tyler",
        "number":45
    }
    return render(request, 'home.html', context)

def contact(request):
    return render(request, 'contacts.html')

def second_page(request):
    #obj = employees.objects.get(id=1)
    context={
        "data":"OBJECT"
    }
    return render(request, 'second_page.html', context)

def upload_and_transcribe(request): # This is the new page for upload
    transcription = "______"
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # save the uploaded file to a temporary location
            file_path = '/home/snick/Temp/' + request.FILES['file'].name
            with open(file_path, 'wb+') as destination:
                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)
            # call the transcriber function with the file path
            transcription = transcriber(file_path)
            #print(transcription)
            context = {
                'form': form,
                'transcription': transcription
            }
    else:
        form = FileUploadForm()
        context = { 'form': form, 'transcription': transcription }
    return render(request, 'upload_and_transcribe.html', context) 

'''
def landingpage(request):
    context = {
        "greeting":"heylo"
    }
    return render(request, 'landingpage.html', context)


def home(request):
    context= {
        "name":"Tyler",
        "number":45
    }
    return render(request, 'home.html', context)


def datepage(request, year):
    article_list = employees.objects.filter(pub_date__year = year)
    context = {
        "year": year,
        "article_list" : article_list
    }
    return render(request, 'datepage.html', context)


def second_page(request):
    obj = employees.objects.get(id=1)
    context={
        "data":obj
    }
    return render(request, 'second_page.html', context)


def contact(request):
    return render(request, 'contacts.html')


def signuppage(request):

    context = {
        "form":registration_forms
    }

    return render(request, 'signup.html', context)


def adduser(request):
    form = registration_forms(request.POST)
    if form.is_valid():
        myregister = registrationdata(username = form.cleaned_data['username'], 
                                    password = form.cleaned_data['password'], 
                                    email = form.cleaned_data['email'], 
                                    phone = form.cleaned_data['phone'])
        myregister.save()
        return redirect('home')
'''