

from typing import Any
from django.urls import reverse
import jwt
from .models import Profile
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

class JWTauthmiddleware:
    def __init__(self , get_response) :
        self.get_response=get_response
        self.excluded_paths = [reverse('loginview'),reverse('registrationsview') ,reverse('messagest'),reverse('studysessionst') ]


    def __call__(self, request) :
        if request.path in self.excluded_paths or request.path.startswith('/admin/'):
            return self.get_response(request)
        
        token = request.COOKIES.get('jwt')

        if not token:
            return JsonResponse({'message':'please sign in'},status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            payload = jwt.decode(token, 'seckey1', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': 'Token expired'}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidTokenError:
            return JsonResponse({'message': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
        

        
        payload = jwt.decode(token , 'seckey1', algorithms=['HS256'])
        


        profile = Profile.objects.filter(user=payload['id']).first()

        if profile.user_type != 'admin':
            return Response({'message':'unauthorised for this action'},status=status.HTTP_401_UNAUTHORIZED)
        
        request.admin =Profile

        return self.get_response(request)