from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def error(request):
    return render(request, 'message.html')

def success(request):
    
    messages.success(request, 'Success Message')    
    return render(request, 'message.html')
def info(request):
    
    messages.info(request, 'Info Message')    
    return render(request, 'message.html')

def danger(request):
    
    messages.error(request, 'Danger Message')    
    return render(request, 'message.html')

def warning(request):
    
    messages.warning(request, 'Warning Message')    
    return render(request, 'message.html')