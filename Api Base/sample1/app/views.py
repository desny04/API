from django.shortcuts import render
from django.http import JsonResponse
from .models import*
from .serializers import*

# Create your views here.

# def fun(request):
#     return JsonResponse({'Name':'Desny','Age': 21,'Address': 'Kochi'})

def fun(request):
    if request.method=='GET':
        d=Students.objects.all()
        s=StudentSerializer(d,many=True)
        return JsonResponse(s.data,safe=False)
