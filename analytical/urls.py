from django.urls import path
from .views import AnalyticalListCreateView, AnalyticalDetailView

urlpatterns = [
    path('api/analyticals/', AnalyticalListCreateView.as_view(), name='analytical-list-create'),
    path('api/analyticals/<uuid:pk>/', AnalyticalDetailView.as_view(), name='analytical-detail'),
]
