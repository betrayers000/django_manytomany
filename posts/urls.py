from django.urls import path
from . import views

app_name="posts"

urlpatterns = [
    path('', views.index, name='index'),
    path('creat/', views.create, name="create"),
    path('<int:id>/like', views.like, name="like"),
]
