from django.shortcuts import render
from .models import User , Subject , StudyGroup , Membership , Message , StudySession , Profile 

# Create your views here.
from .serializers import UserSerilizers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from datetime import timedelta
import datetime , jwt
from rest_framework import generics

from django.contrib.auth import login , logout
from .serializers import SubjectSerilizers , MembershipSerilizers , MessageSerilizers , StudySessionSerilizers  , StudyGroupSerilizers

class RegistrationView(APIView):
    def post(self, request):
     
        serializer = UserSerilizers(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            profile = Profile(user=user , user_type = request.data.get('user_type'))
            profile.save()
            return Response({'message':'signup successfull', 'data':request.data} , status=status.HTTP_200_OK)
        
        return Response({'message':'invalid credential'} , status=status.HTTP_406_NOT_ACCEPTABLE)


class LoginView(APIView):
    def post(self, request):
        username= request.data.get('username')
        password= request.data.get('password')

        user = User.objects.filter(username=username).first()

        if user is None:
            return Response({'message':'invalid username'} , status=status.HTTP_400_BAD_REQUEST)
        
        if not user.check_password(password):
            return Response({'message':'invalid password'} , status=status.HTTP_400_BAD_REQUEST)
        
        login(request  , user)

        payload = {
            'id':user.id,
            'exp':datetime.datetime.now(datetime.UTC) + timedelta(minutes=90),
            'iat':datetime.datetime.now(datetime.UTC)
        }

        token = jwt.encode(payload , 'seckey1' , algorithm='HS256')

        response = Response()
        response.data = {
            'message':'signin successfull',
            'token':token
        }

        response.status = status.HTTP_200_OK

        response.set_cookie(
            key='jwt',
            value=token,
            httponly=False,
            samesite=None,
            secure=None

        )

        return response

class LogoutView(APIView):
    def post(self, request):
        logout(request)

        response = Response()
        response.data ={'message':'log out successfull'}
        response.status = status.HTTP_200_OK

        response.delete_cookie('jwt')

        return response



class SubjectView(APIView):
    def get(self , request):
        subjects = Subject.objects.all()
        serializer = SubjectSerilizers(subjects , many=True)
       
        
        return Response({'message':'subject created', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        
        
    def post(self , request):
        
        # request.data['admin']=request.admin.id
        serializer = SubjectSerilizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'subject created'}, status=status.HTTP_201_CREATED)
        
        return Response({'message':'invalid syntex'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def put(self , request , *args , **kwargs):
        sub_id = kwargs.get('id')
        sub= Subject.objects.filter(id=sub_id).first()
        
        serializer = SubjectSerilizers(sub,data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'subject updated'}, status=status.HTTP_201_CREATED)
        
        return Response({'message':'invalid syntex'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    

    def delete(self , request , *args , **kwargs):
        sub_id = kwargs.get('id')
        sub= Subject.objects.filter(id=sub_id).first()
        
        sub.delete()
        return Response({'message':'sub deleted'}, status=status.HTTP_200_OK)
    

class StudyGroupView(APIView):
    def get(self , request):
        studygroup = StudyGroup.objects.all()
        serializer = StudyGroupSerilizers(studygroup , many=True)
       
        return Response({'data':serializer.data}, status=status.HTTP_201_CREATED)
        
        
    def post(self , request):
        
        serializer = StudyGroupSerilizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'study group added created'}, status=status.HTTP_201_CREATED)
        
        return Response({'message':'invalid syntex'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def put(self , request , *args , **kwargs):
        group_id = kwargs.get('id')
        group= StudyGroup.objects.filter(id=group_id).first()
        
        serializer = SubjectSerilizers(group,data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'group updated'}, status=status.HTTP_201_CREATED)
        
        return Response({'message':'invalid syntex'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    

    def delete(self , request , *args , **kwargs):
        group_id = kwargs.get('id')
        group= StudyGroup.objects.filter(id=group_id).first()
        
        group.delete()
        return Response({'message':'group deleted'}, status=status.HTTP_200_OK)
    




class MembershipView(APIView):
    def get(self , request):
        membership = Membership.objects.all()
        serializer = MembershipSerilizers(membership , many=True)
       
        return Response({'data':serializer.data}, status=status.HTTP_201_CREATED)
        
        
    def post(self , request):
        
        serializer = MembershipSerilizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'membership added'}, status=status.HTTP_201_CREATED)
        
        return Response({'message':'invalid syntex'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    
    def put(self , request , *args , **kwargs):
        mem_id = kwargs.get('id')
        mem= Membership.objects.filter(id=mem_id).first()
        
        serializer = MembershipSerilizers(mem,data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'membership updated'}, status=status.HTTP_201_CREATED)
        
        return Response({'message':'invalid syntex'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    

    def delete(self , request , *args , **kwargs):
        mem_id = kwargs.get('id')
        mem= Membership.objects.filter(id=mem_id).first()
        
        mem.delete()
        return Response({'message':'membership deleted'}, status=status.HTTP_200_OK)
    




class MessageView(APIView):
    def get(self , request):
        message = Message.objects.all()
        serializer = MessageSerilizers(message , many=True)
       
        return Response({'data':serializer.data}, status=status.HTTP_201_CREATED)
        
        
    def post(self , request):
        
        serializer = MessageSerilizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'message created'}, status=status.HTTP_201_CREATED)
        
        return Response({'message':'invalid syntex'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    

    def put(self , request , *args , **kwargs):
        message_id = kwargs.get('id')
        messsage= Message.objects.filter(id=message_id).first()
        
        serializer =MessageSerilizers(messsage,data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'message updated'}, status=status.HTTP_201_CREATED)
        
        return Response({'message':'invalid syntex'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    

    def delete(self , request , *args , **kwargs):
        message_id = kwargs.get('id')
        messsage= Message.objects.filter(id=message_id).first()

        messsage.delete()
        return Response({'message':'message deleted'}, status=status.HTTP_200_OK)
    

class StuddySessionView(APIView):
    def get(self , request):
        study_sessions =  StudySession.objects.all()
        serializer =StudySessionSerilizers(study_sessions , many=True)
       
        
        return Response({'data':serializer.data}, status=status.HTTP_201_CREATED)
        
        
    def post(self , request):
        
        
        serializer = StudySessionSerilizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'studdy session created'}, status=status.HTTP_201_CREATED)
        
        return Response({'message':'invalid syntex'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    

    def put(self , request , *args , **kwargs):
        session_id = kwargs.get('id')
        session= StudySession.objects.filter(id=session_id).first()
        
        serializer =StudySessionSerilizers(session,data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'study session updated'}, status=status.HTTP_201_CREATED)
        
        return Response({'message':'invalid syntex'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    

    def delete(self , request , *args , **kwargs):
        session_id = kwargs.get('id')
        session= StudySession.objects.filter(id=session_id).first()

        session.delete()
        return Response({'message':'session deleted'}, status=status.HTTP_200_OK)
    


from rest_framework.pagination import PageNumberPagination
from rest_framework import filters 
from django_filters.rest_framework import DjangoFilterBackend


class CustomPagination(PageNumberPagination):
    page_size = 4



class MessageViewST(generics.ListAPIView):
    queryset= Message.objects.all()
    serializer_class = MessageSerilizers
    filter_backends = [DjangoFilterBackend ,filters.OrderingFilter  ]
    ordering_fields =  ['study_group']
    filterset_fields=  ['study_group']
    pagination_class = CustomPagination

   
    

class StudySessionViewST(generics.ListAPIView):
    queryset= StudySession.objects.all()
    serializer_class = StudySessionSerilizers
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend ,filters.OrderingFilter  ]
    ordering_fields =  ['study_group' ,'created_at']
    filterset_fields=  ['study_group','title']







   