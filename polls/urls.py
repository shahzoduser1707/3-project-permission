from django.urls import path
from .views import ListAuthorApiView,DetailUpdateDestroyAuthorView



urlpatterns = [
    path('all/',ListAuthorApiView.as_view()),
    path('detail/<int:pk>',DetailUpdateDestroyAuthorView.as_view())
]