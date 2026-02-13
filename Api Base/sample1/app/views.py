from django.shortcuts import render
from django.http import JsonResponse
from .models import*
from .serializers import*
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.

# def fun(request):
#     return JsonResponse({'Name':'Desny','Age': 21,'Address': 'Kochi'})

# def fun(request):
#     if request.method=='GET':
#         d=Students.objects.all()
#         s=StudentSerializer(d,many=True)
#         return JsonResponse(s.data,safe=False)

@csrf_exempt
def fun(request):
    if request.method=='GET':
        d=Students.objects.all()
        s=StudentModelSerializer(d,many=True)
        return JsonResponse(s.data,safe=False)
    elif request.method=='POST':
        d=JSONParser().parse(request)
        s=StudentModelSerializer(data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.error)



