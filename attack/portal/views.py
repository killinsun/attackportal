from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms


def mainpage(request):
    if request.user.is_authenticated():
        username    = request.user.username
        firstName   = request.user.first_name   
        lastName    = request.user.last_name   
    else:
        username    = "null"
        firstName   = "null",
        lastName    = "null",

    parms = {
        'username'  : username,
        'firstName' : firstName,
        'lastName'  : lastName,
        'debug'     : "ture!!!!!!",
        }

    return render(request, 'portal/index.html',parms) 
    
@login_required
def vmlist(request):
    return render(request, 'portal/vmlist.html', {})

@login_required
def deploy(request):
    return render(request, 'portal/deploy.html', {})
    
    
@login_required
def mypage(request):
    return render(request, 'portal/mypage.html')

@login_required
def redirect(request):
    return render(request, 'portal/redirect.html')

