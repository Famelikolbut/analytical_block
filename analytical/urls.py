from django.urls import path
from .views import AnalyticalListCreateView, AnalyticalDetailView

urlpatterns = [
    path('analyticals/', AnalyticalListCreateView.as_view(), name='analytical_list_create'),
    path('analyticals/<uuid:pk>/', AnalyticalDetailView.as_view(), name='analytical_detail'),
]
