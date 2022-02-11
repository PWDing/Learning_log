"""为learning_logs应用定义URL模式"""

from django.urls import path
from . import views


app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('entries/', views.entries, name='entries'),
]