import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Details


# Create your views here.
@csrf_exempt
def add_details(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('name')
        phn_num = data.get('phn_num')
        aadhar_num = data.get('aadhar_num')
        pan_num = data.get('pan_num')
        passport_num = data.get('passport_num')
        details = Details.objects.create(name=name, phn_num=phn_num, aadhar_num=aadhar_num, pan_num=pan_num,
                                         passport_num=passport_num)
        details.save()
        return JsonResponse({'message': 'Details saved'})


def read_details(request):
    details=Details.objects.all().values()
    return JsonResponse({"data":list(details)})
