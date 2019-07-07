from Kariz import views
from .models import User
from . import views
from django.urls import path , include
from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    #path('', views.index , name= 'index'),
    #path('test/', views.test),
    #path('signup/', views.signup.as_view()),
    #path('search\(?p<test>\w{0,50})',views.funcname.as_view())
    path('signup/', views.signup.as_view(), name='signup'),
    path('createproject/', views.createproject.as_view(), name='Create project'),
    path('projectlist/<category>/', views.projectlisthandler.as_view(), name='Project list'),
    path('project/<id>/', views.projectlhandler.as_view(), name='Project'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('dashboard/', views.dashboardhandler.as_view()),
    path('search/<name>/', views.searchhandler.as_view(), name='search'),

]