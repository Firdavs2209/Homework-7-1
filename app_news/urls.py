
from django.urls import path
from . import views





urlpatterns = [
    path('create/', views.create_news, name='create'),
    path('update/', views.update_news, name='update'),
    path('delete/', views.delete_news, name='delete'),
]
