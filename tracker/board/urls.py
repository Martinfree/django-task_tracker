"""tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include

from board.views import (BoardsAPIView, BoardAPIView, TasksAPIView,
                         TaskAPIView, TasksFilterAPIView)


urlpatterns = [
        #Board model api
        path('board/',BoardsAPIView.as_view(),name='boards'),    
        path('board/<int:id>/', BoardAPIView.as_view(),name='board'),    
        
        #Task model api
        path('task/', TasksAPIView.as_view(),name='tasks'),    
        path('task/filter/', TasksFilterAPIView.as_view(),name='task_filter'),  
        path('task/filter/<int:id>/', TasksFilterAPIView.as_view(),name='task_filter'),  
        path('task/<int:id>/', TaskAPIView.as_view(),name='task'),  
]


