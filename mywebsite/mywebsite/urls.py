"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name = 'index'),#This is connecting to the views file check what is in the index function
#     path('about/', views.about, name = 'about'),
#     path('more/',views.test_task, name='more'),
#     path('task2/',views.task2, name = 'task2'),
#     #This is going to get the about function in views.py file
# ] This code is for video 6 now time for video 7 in which we add pipe
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index, name = 'index'),
#     path('removepunc', views.removepunc, name='rempun'),
#     path('capitalizefirst', views.capfirst, name='capfirst'),
#     path('newlineremove', views.newlineremove, name='newlineremove'),
#     path('spaceremove', views.spaceremove, name='spaceremove'),
#     path('charcount', views.charcount, name='charcount'),
## ]
#Above code is of video 7 and I also completed the challange now it's time to add templates in video 8
#first go to settings.py and 'DIRS': ["templates"], do this ten we are able to addd templates
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('removepunc', views.removepunc, name='rempun'),
#     path('capitalizefirst', views.capfirst, name='capfirst'),
#     path('newlineremove', views.newlineremove, name='newlineremove'),
#     path('spaceremove', views.spaceremove, name='spaceremove'),
#     path('charcount', views.charcount, name='charcount'),
#
# ]
#Now the code is for video 10

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('analyze', views.analyze, name='analyze'),
#     path('Calculator', views.Calculator, name='Calculator'),
# ]
#Now adding and making a complete website for text parsing:
urlpatterns=[
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
    path('about', views.about, name='about/')
]