
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user_role=(('teacher','teacher'),('admin' , 'admin'),('student','student'))
    user= models.OneToOneField(User , on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=user_role , default='student')
    
    def __str__(self) -> str:
        return f'{self.user.username}--{self.user_type}'

    
class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class StudyGroup(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='study_groups')
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(User, through='Membership')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.subject}'

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'study_group')
    
    def __str__(self):
        return f"{self.user.username} in {self.study_group.name}"


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.user.username} in {self.study_group.name}"


class StudySession(models.Model):
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='study_sessions')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} in {self.study_group.name}"

