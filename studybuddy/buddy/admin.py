from django.contrib import admin

# Register your models here.

from .models import  Profile, Subject , StudyGroup , Membership , Message , StudySession


admin.site.register(Profile)
admin.site.register(Subject)
admin.site.register(StudyGroup)
admin.site.register(Membership)
admin.site.register(Message)
admin.site.register(StudySession)
