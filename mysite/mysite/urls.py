"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from polls import views
from django.urls import path, include
#from django.conf.urls import include
#from mysite.views import UserCreateView
from mysite import mviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', views.IndexView.as_view(), name="index"),
    path('polls/<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('polls/<int:question_id>/vote/', views.vote, name="vote"),
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name="results"),
    path('parent/', views.TemplateParentView.as_view(), name='parent'),
    path('child/', views.TemplateChildView.as_view(), name='child'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', mviews.UserCreateView.as_view(), name='registration'),
    path('session/', mviews.SessionTestView.as_view(), name="session"),

#    path('polls/', views.index, name="index"),
#    path('polls/<int:question_id>/', views.detail, name="detail"),
#    path('polls/<int:question_id>/vote/', views.vote, name="vote"),
#    path('polls/<int:question_id>/results/', views.results, name="results"),
]
