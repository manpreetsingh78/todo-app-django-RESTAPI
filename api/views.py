from .models import ToDoList
from .serializers import ToDoSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication , TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
#---------------------------Using Model View Set---------------------------

class TodoViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoSerializer
    authentication_classes = [BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    # authentication_classes = [CustomAuthentication]
    # # permission_classes = [Allowany] To overrid global
    
    #---------USER AUTHENTICITY---------
    def get_queryset(self):
        user = self.request.user.id
        return ToDoList.objects.filter(user=user)

    #--------FILTERS---------
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['status','tags','due_date']
    search_fields = ['title']
    
    
    
#---------------------------Using View Set---------------------------

# class TodoViewSet(viewsets.ViewSet):
#     def list(self,request):
#         print("Basename:",self.basename)
#         print("Action:",self.action)
#         print("Details:",self.detail)
#         print("Suffix:",self.suffix)
#         print("Name:",self.name)
#         print("Dsc:",self.description)
#         stu = ToDoList.objects.all()
#         serializer= ToDoSerializer(stu,many=True)
#         return Response(serializer.data)
#     def retrieve(self,request,pk=None):
#         id = pk
#         if id is not None:
#             stu = ToDoList.objects.get(pk=id)
#             serializer= ToDoSerializer(stu)
#             return Response(serializer.data)
#     def create(self,request):
#         serializer = ToDoSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def update(self,request,pk=None):
#         id = pk
#         stu = ToDoList.objects.get(pk=id)
#         serializer= ToDoSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Updated'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def destroy(self,request,pk=None):
#         id = pk
#         stu = ToDoList.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'} )


#---------------------------Using Generix View---------------------------

# from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView

# class ToDoListAPI_LC(ListCreateAPIView):
#     queryset = ToDoList.objects.all()
#     serializer_class = ToDoListSerializer
# class ToDoListAPI_RUD(RetrieveUpdateDestroyAPIView):
#     queryset = ToDoList.objects.all()
#     serializer_class = ToDoListSerializer

#--------------------------- Using Mixin Model---------------------------

# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin
# class ToDoListAPI(GenericAPIView,ListModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin):
#     queryset = ToDoList.objects.all()
#     serializer_class = ToDoListSerializer
#     # def get(self,request,*args, **kwargs):
#     #     return self.list(request,*args, **kwargs)
#     def get(self,request,pk=None,*args, **kwargs):
#         if pk is not None:
#             return self.retrieve(request,*args, **kwargs)
#         return self.list(request,*args, **kwargs)
        
#     def post(self,request,*args, **kwargs):
#         return self.create(request,*args, **kwargs)

#     def put(self,request,pk,*args, **kwargs):
#         return self.update(request,*args, **kwargs)
#     def delete(self,request,pk,*args, **kwargs):
#         return self.destroy(request,*args, **kwargs)


#---------------------------using decorators API VIEW---------------------------

# import io
# from django.views import View
# from .serializers import ToDoSerializer
# from .models import ToDoList
# from django.http import HttpResponse, JsonResponse
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

# # Create your views here.
# @method_decorator(csrf_exempt ,name='dispatch')
# class ToDoListAPI(View):
#     def get(self,request,*args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id',None)
#         if id is not None:
#             stu = ToDoList.objects.get(id=id)
#             serializer = ToDoSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
            
#         stu = ToDoList.objects.all()
#         serializer = ToDoSerializer(stu,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     def post(self,request,*args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = ToDoSerializer(data = python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'DATA CREATED'}
#             return JsonResponse(res,safe=False)
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
#     def put(self,request,*args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         stu = ToDoList.objects.get(id=id)
#         serializer = ToDoSerializer(stu,data = python_data,partial=True)
        
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'updated successfully'}
#             return JsonResponse(res,safe=False)
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
#     def delete(self,request,*args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         stu = ToDoList.objects.get(id=id)
#         stu.delete()
#         res = {'msg':'deleted successfully'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data,content_type='application/json')
#         return JsonResponse(res,safe=False)















