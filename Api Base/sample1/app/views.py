from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import*
from .serializers import*
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,mixins

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


# @api_view(['GET','POST','PUT','DELETE'])
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
#             return JsonResponse(s.data,status=status.HTTP_201_CREATED)
#         else:
#             return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method=='DELETE':
#         demo.delete()
#         return HttpResponse('Deleted')

# class fun(APIView):
#     def get(self,request):
#         demo=Students.objects.all()
#         s=StudentModelSerializer(demo,many=True)
#         return Response(s.data)
#     def post(self,request):
#         s=StudentModelSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

# class fun(APIView):
#     def get(self,request,d):
#         try:
#             demo=Students.objects.get(pk=d)
#         except:
#             return Response('Student not found')

#         def get(self,request):
#             s=StudentModelSerializer(demo)
#             return Response(s.data,safe=False)
#         def put(self,request):
#             d=JSONParser().parse(request)
#             s=StudentModelSerializer(demo,data=d)
#             if s.is_valid():
#                 s.save()
#                 return Response(s.data)
#             else:
#                 return Response(s.errors)
#         def delete(self,request):
#             demo.delete()
#             return Response('Deleted')


# class fun8(APIView):
#     def get(self,req,d):
#         try:
#             demo=Students.objects.get(pk=d)
#             s=StudentModelSerializer(demo)
#             return Response(s.data)
#         except Students.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#     def put(self,req,d):
#         try:
#             demo=Students.objects.get(pk=d)
#             s=StudentModelSerializer(demo,data=req.data)
#             if s.is_valid():
#                 s.save()
#                 return Response(s.data)
#             else:
#                 return Response(status=status.HTTP_400_BAD_REQUEST)
#         except Students.DoesNotExist:
#             return response(status=status.HTTP_404_NOT_FOUND)
#     def delete(self,req,d):
#         try:
#             demo=Students.objects.get(pk=d)
#             demo.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)

# class genericapiview(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
#     serializer_class=StudentModelSerializer
#     queryset=Students.objects.all()
#     def get(self,req):
#         return self.list(req)
#     def post(self,req):
#         return self.create(req)

class update(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=StudentModelSerializer
    queryset=Students.objects.all()
    lookup_field='id'
    def get(self,req,id=None):
        return self.retrieve(req)
    def put(self,req,id=None):
        return self.update(req,id)
    def delete(self,req,id):
        return self.destroy(req,id)