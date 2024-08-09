from rest_framework import serializers
from .models import  Profile, Subject , StudyGroup , Membership , Message , StudySession
from django.contrib.auth.models import User

class UserSerilizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id' , 'username','password']
    
    def create(self , validated_data):
        instance = self.Meta.model(**validated_data)

        password = validated_data.pop('password' , None)

        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance

class ProfileSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ='__all__'

class SubjectSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields ='__all__'



class StudyGroupSerilizers(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields ='__all__'

class MembershipSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields ='__all__'



class MessageSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields ='__all__'

class StudySessionSerilizers(serializers.ModelSerializer):
    class Meta:
        model = StudySession
        fields ='__all__'