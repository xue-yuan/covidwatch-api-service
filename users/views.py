from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as d_login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import forms
from .models import UploadData

# Create your views here.

@csrf_exempt
def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            d_login(request, user)
            return HttpResponse(status=200)
    return HttpResponse(status=403)

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = forms.RegisterForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('user_register_success')
    return render(request, 'register.html', context=locals())

def register_success(request):
    return render(request, 'register_success.html', locals())

@csrf_exempt
def upload_data(request):
    if request.POST:
        strength = request.POST.get('strength')
        fk_exp_id = request.POST.get('fk_exp_id')
        battery_level = request.POST.get('battery_level')

        data = UploadData(strength=strength, fk_exp_id=fk_exp_id, battery_level=battery_level)
        data.save()
        return HttpResponse(status=200)
    return HttpResponse(status=403)