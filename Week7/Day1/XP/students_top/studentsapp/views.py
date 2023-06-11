from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response #connect to Django bulit in template system
from rest_framework.permissions import AllowAny

from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from django.http import Http404

from .models import Student

from studentsapp.serializers import StudentSerializer

# Create your views here.


#student_list 
class StudentListView(APIView):
    
    permission_classes = (AllowAny,)
    
    def get(self, request, *args, **kwargs):
        # print(args)
        # print(kwargs)  {'pk': 1}
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many = True)
        return  Response(serializer.data)
    
    def post(self, request, *args, **kwargs):  #add to admin page field with button post
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#student_detail 
class StudentDetailView(APIView):
    
    def get(self, request, pk, *args, **kwargs):
        try:
            report = Student.objects.get(id = pk)
            serializer = StudentSerializer(report)
            return  Response(serializer.data)
        except:
            raise Http404
       
    #update/put
    def put(self, request, pk, *args, **kwargs):
        post = Student.objects.get(id=pk)
        serializer = StudentSerializer(post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    #delete
    def delete(self, request, pk, *args, **kwargs):
        post = Student.objects.get(id=pk)
        post.delete()
        return Response(status= HTTP_204_NO_CONTENT)


# main
# class StudentView(APIView):
    
#     def get(self, request, *args, **kwargs):
#         # print(args)
#         # print(kwargs)  {'pk': 1}
#         if 'pk' in kwargs:
#             report = Student.objects.get(id = kwargs['pk'])
#             serializer = StudentSerializer(report)
#             return  Response(serializer.data)
#         else:
#             queryset = Student.objects.all()
#             serializer = StudentSerializer(queryset, many = True)
#             return  Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):  #add to admin page field with button post
#         serializer = StudentSerializer(data = request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data = serializer.data)
#         return Response(serializer.errors)
    
    
#     #delete
#     def delete(self, request, pk, *args, **kwargs):
#         post = Student.objects.get(id=pk)
#         post.delete()
#         return Response()
    
        
#     #update/put
#     def put(self, request, pk, *args, **kwargs):
#         post = Student.objects.get(id=pk)
#         serializer = StudentSerializer(post, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)