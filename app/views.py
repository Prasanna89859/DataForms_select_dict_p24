from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse



def dateforms(request):
    ENFO=Nameform()
    d={'ENFO':ENFO}
    if request.method == 'POST':
        NFDO=Nameform(request.POST)
        if NFDO.is_valid():
            return HttpResponse(str(NFDO.cleaned_data))
        else:
            return HttpResponse('Data is not valid')
        
    return render(request,'dateforms.html',d)
