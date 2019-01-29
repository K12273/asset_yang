from django.urls import path,include
from . import views

app_name='cms'
urlpatterns = [
    path('',views.blog_title,name="blog_title"),
]