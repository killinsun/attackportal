from django.shortcuts import render
from django.http  import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from portal.lib.manage_esxi import *


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
    if request.method == 'POST':
        form = forms.deployVmForm(request.POST)
        if form.is_valid():
            vm_name = form.cleaned_data['VM_name']
            os_type = form.cleaned_data['OS_type']
            connect_test(vm_name,os_type)
            #form.cleaned_data process
            # ...
            #return HttpResponseRedirect('/complete_deploy/')
            return render(request, 'portal/complete_deploy.html', {'vm_name':vm_name,'os_type':os_type})
    else:
        form = forms.deployVmForm()

    return render(request, 'portal/deploy.html', {'form':form,})
    

@login_required
def completeDeploy(request):
    return render(request, 'portal/complete_deploy.html')
    
@login_required
def mypage(request):
    return render(request, 'portal/mypage.html')

@login_required
def redirect(request):
    return render(request, 'portal/redirect.html')

