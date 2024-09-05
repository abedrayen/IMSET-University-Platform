from django.urls import path
from . import views

urlpatterns = [
    path('diploma/<int:diploma_id>/', views.generate_diploma, name='generate_diploma'),
    path('preview/<int:diploma_id>/', views.preview_diploma, name='preview_diploma'),
]
