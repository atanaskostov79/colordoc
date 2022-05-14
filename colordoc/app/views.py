from urllib import request
from django.shortcuts import render, redirect
from .models import Document, TxtToDoc
from .forms import DocumentForm, TxtToDoc, TxtToDocForm
from .functions import  colorfile, textToDoc  

def index(request):
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            
            
            fs = form.save()
            print(fs.document.name)
            file = colorfile(fs.document.name)  
            context = {'form': form, 'file': file}
            return render(request, 'app/index.html', context )
    else:
        
        return render(request, 'app/index.html', {'form': form})

def fromtext(request):
    # form = TxtToDocForm()
    form = TxtToDocForm(request.POST)
    
    if request.method == 'POST':
        

        if form.is_valid():
            fs = form.save()
            
            file =  textToDoc(fs.text)
            print(file)
            context = {'form': form , 'file': file}
            return render(request, 'app/text.html', context)
    else:
       
        return render(request, 'app/text.html', {'form': form})