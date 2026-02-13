from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import*
from .serializers import*
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# def fun(request):
#     return JsonResponse({'Name':'Desny','Age': 21,'Address': 'Kochi'})

# def fun(request):
#     if request.method=='GET':
#         d=Students.objects.all()
#         s=StudentSerializer(d,many=True)
#         return JsonResponse(s.data,safe=False)

# @csrf_exempt
# def fun(request):
#     if request.method=='GET':
#         d=Students.objects.all()
#         s=StudentModelSerializer(d,many=True)
#         return JsonResponse(s.data,safe=False)
#     elif request.method=='POST':
#         d=JSONParser().parse(request)
#         s=StudentModelSerializer(data=d)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data)
#         else:
#             return JsonResponse(s.error)

# @csrf_exempt
# def fun(request,d):
#     try:
#         demo=Students.objects.get(pk=d)
#     except:
#         return HttpResponse('Student not found')

#     if request.method=='GET':
#         s=StudentModelSerializer(demo)
#         return JsonResponse(s.data,safe=False)
#     elif request.method=='PUT':
#         d=JSONParser().parse(request)
#         s=StudentModelSerializer(demo,data=d)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data)
#         else:
#             return JsonResponse(s.errors)
#     elif request.method=='DELETE':
#         demo.delete()
#         return HttpResponse('Deleted')


# @api_view(['GET','POST'])
# def fun(request):
#     if request.method=='GET':
#         d=Students.objects.all()
#         s=StudentModelSerializer(d,many=True)
#         return Response(s.data)
#     elif request.method=='POST':
#         d=JSONParser().parse(request)
#         s=StudentModelSerializer(data=d)
#         if s.is_valid():
#             s.save()
#             return JsonResponse(s.data,status=status.HTTP_201_CREATED)
#         else:
#             return JsonResponse(s.error,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','PUT','DELETE'])
def fun(request,d):
    try:
        demo=Students.objects.get(pk=d)
    except:
        return HttpResponse('Student not found')

    if request.method=='GET':
        s=StudentModelSerializer(demo)
        return JsonResponse(s.data,safe=False)
    elif request.method=='PUT':
        d=JSONParser().parse(request)
        s=StudentModelSerializer(demo,data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        demo.delete()
        return HttpResponse('Deleted')


