from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from .models import Analytical
from .schemas import analytical_list_create_structure
from .serializers import AnalyticalSerializer


class AnalyticalListCreate(generics.ListCreateAPIView):
    queryset = Analytical.objects.all()
    serializer_class = AnalyticalSerializer

    @swagger_auto_schema(manual_parameters=[analytical_list_create_structure])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
