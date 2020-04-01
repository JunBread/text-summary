from django.urls import path, include
from app import views
from django.contrib import admin

urlpatterns = [
    path('', views.demo, name='demo'),
    path('eval', views.eval, name='eval'),
    path('score', views.avg_eval, name='score_eval'),
    path('admin/', admin.site.urls),
]