from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as d_login
from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

import json
import secrets
import datetime

from . import forms
from .models import UploadData, User
from .models import TCN_RX, TCN_TX, AttackLog, GlobalSetting
# Create your views here.

@csrf_exempt
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = forms.RegisterForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('user_register_success')
    else:
        print(request.POST)
    return render(request, 'register.html', context=locals())

def register_success(request):
    return render(request, 'register_success.html', locals())

@csrf_exempt
def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        uuid = request.POST.get('uuid')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.uuid is None:
                user.uuid = uuid
                user.save()
            elif user.uuid != uuid:
                return JsonResponse({
                    'success': False, 
                    'message': 'Wrong UUID'
                })
            d_login(request, user)
            token = secrets.token_urlsafe(32)
            expire_time = datetime.datetime.now() + datetime.timedelta(days=3)
            user.token = token
            user.expire_time = expire_time
            user.last_api_calling = datetime.datetime.now()
            user.save()
            return JsonResponse({
                'success': True, 
                'token': token
            })
        else:
            return JsonResponse({
                'success': False, 
                'message': 'User Not Found'
            })
    return JsonResponse({
        'success': False, 
        'message': 'Wrong Method'
    })

@csrf_exempt
def upload_tcn_rx(request):
    data = json.loads(request.body)
    uuid = data['uuid']
    token = data['token']
    user = User.objects.get(uuid=uuid)
    
    if user.token == token:
        if user.expire_time < datetime.datetime.now():
            return JsonResponse({
                'success': False, 
                'message': 'Token Expired'
            })
        else:
            expire_time = datetime.datetime.now() + datetime.timedelta(days=3)
            user.expire_time = expire_time
            user.save()
    else:
        return JsonResponse({
            'success': False, 
            'message': 'Invalid Token'
        })

    if request.method == 'POST':
        setting = GlobalSetting.objects.get(id=1)
        for record in data['TCN_RX']:
            try:
                tcn_rx = TCN_RX(
                    rx_muuid_short=record['RX_MUUID_SHORT'],
                    tx_muuid_short=record['TX_MUUID_SHORT'],
                    tx_muuid=record['TX_MUUID'],
                    rx_tcn=record['RX_TCN'],
                    tcn=record['TCN'],
                    rssi=record['RSSI'],
                    distance=record['DISTANCE'],
                    unix_timestamp=datetime.datetime.fromtimestamp(record['UNIX_TIMESTAMP']),
                    upload_timestamp=datetime.datetime.now(),
                    exp_id=setting.exp_id
                )
                tcn_rx.save()
            except:
                return JsonResponse({
                    'success': False, 
                    'message': 'Invalid Field or Data'
                })
        user.last_api_calling = datetime.datetime.now()
        user.save()
        return JsonResponse({
            'success': True
        })
    return JsonResponse({
        'success': False, 
        'message': 'Wrong Method'
    })

@csrf_exempt
def upload_tcn_tx(request):
    data = json.loads(request.body)
    uuid = data['uuid']
    token = data['token']
    user = User.objects.get(uuid=uuid)
    
    if user.token == token:
        if user.expire_time < datetime.datetime.now():
            return JsonResponse({
                'success': False, 
                'message': 'Token Expired'
            })
        else:
            expire_time = datetime.datetime.now() + datetime.timedelta(days=3)
            user.expire_time = expire_time
            user.save()
    else:
        return JsonResponse({
            'success': False, 
            'message': 'Invalid Token'
        })

    if request.method == 'POST':
        setting = GlobalSetting.objects.get(id=1)
        for record in data['TCN_TX']:
            try:
                tcn_tx = TCN_TX(
                    tx_muuid_short=record['TX_MUUID_SHORT'],
                    tx_muuid=record['TX_MUUID'],
                    tx_tcn=record['TX_TCN'],
                    own_tcn=record['OWN_TCN'],
                    battery_level=record['BATTERY_LEVEL'],
                    motion_status=record['MOTION_STATUS'],
                    gps_status=record['GPS_STATUS'],
                    unix_timestamp=datetime.datetime.fromtimestamp(record['UNIX_TIMESTAMP']),
                    upload_timestamp=datetime.datetime.now(),
                    exp_id=setting.exp_id
                )
                tcn_tx.save()
            except:
                return JsonResponse({
                    'success': False, 
                    'message': 'Invalid Field or Data'
                })
        user.last_api_calling = datetime.datetime.now()
        user.save()
        return JsonResponse({
            'success': True
        })
    return JsonResponse({
        'success': False, 
        'message': 'Wrong Method'
    })

@csrf_exempt
def upload_attack_log(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        for record in data:
            print(record)
            try:
                attack = AttackLog(
                    blind_log=record['blindLog'], 
                    unix_timestamp=datetime.datetime.fromtimestamp(record['UNIX_TIMESTAMP'])
                )
                attack.save()
            except:
                return JsonResponse({'success': False})
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@csrf_exempt
def update_exp_id(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        exp_id = data['exp_id']
        setting, created = GlobalSetting.objects.get_or_create(id=1)
        setting.exp_id = exp_id
        setting.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def apk_download(request):
    file = open('static/assets/contact-tracing.apk','rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="contact-tracing.apk"'
    return response