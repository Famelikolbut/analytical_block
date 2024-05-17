from django.urls import path

from . import views

urlpatterns = [
    path('analytical/', views.AnalyticalListCreate.as_view(), name='analytical'),
]
