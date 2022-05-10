from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from .functions import  colorfile  

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