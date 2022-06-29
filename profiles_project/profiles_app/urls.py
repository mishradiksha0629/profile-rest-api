from django.urls import path
from profiles_app import views

urlpatterns = [
    path('hello-api/',views.HelloApiView.as_view()),
]
