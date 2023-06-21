from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('api/analyze/', views.analyze, name='analyze'),
    path('api/analyze/all/', views.all_analyzed, name='all'),
    
]