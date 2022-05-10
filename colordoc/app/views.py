from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from .functions import handle_uploaded_file  

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            
            handle_uploaded_file(request.FILES['document'])  
            fs = form.save()
            for ss in fs:
                print(ss)
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'app/index.html', {
        'form': form
    })