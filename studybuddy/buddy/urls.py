
from django.urls import path
from .views import RegistrationView , LoginView , SubjectView , LogoutView , StudyGroupView , MembershipView , MessageView , StuddySessionView

from .views import StudySessionViewST , MessageViewST

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('registration/', RegistrationView.as_view(), name='registrationsview'),
    path('login/',LoginView.as_view(), name='loginview'),
    path('logout/',LogoutView.as_view(), name='logout'),

    path('subject/',SubjectView.as_view(), name='subject'),
    path('subject/<int:id>/',SubjectView.as_view(), name='subject'),
    

    path('studygroup/',StudyGroupView.as_view(), name='studygroup'),
    path('studygroup/<int:id>/',StudyGroupView.as_view(), name='studygroup_update_delete'),

    path('membership/',MembershipView.as_view(), name='membership'),
    path('membership/<int:id>/',MembershipView.as_view(), name='membership_update_delete'),

    path('membership/',MembershipView.as_view(), name='membership'),
    path('membership/<int:id>/',MembershipView.as_view(), name='membership_update_delete'),
    

    path('message/',MessageView.as_view(), name='message'),
    path('message/<int:id>/',MessageView.as_view(), name='message_update_delete'),
    

    path('session/',StuddySessionView.as_view(), name='session'),
    path('session/<int:id>/',StuddySessionView.as_view(), name='session_update_delete'),
    
    

    path('messageST/',MessageViewST.as_view(), name='messagest'),
    path('studysessionST/',StudySessionViewST.as_view(), name='studysessionst'),
]



