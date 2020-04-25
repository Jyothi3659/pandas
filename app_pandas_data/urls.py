from django.urls import path
from .views  import StudentView

urlpatterns = [
    path('library/', StudentView.as_view()),

]