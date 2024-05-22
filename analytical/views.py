from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from drf_yasg.utils import swagger_auto_schema
from .models import Analytical
from .serializers import AnalyticalSerializer


class AnalyticalListCreateView(APIView):
    parser_classes = [JSONParser]

    @swagger_auto_schema(
        operation_description="Get all analyticals",
        operation_summary="Get all analyticals",
        responses={200: AnalyticalSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        queryset = Analytical.objects.all().order_by("name")
        serializer = AnalyticalSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new analytical",
        operation_summary="Create a new analytical",
        request_body=AnalyticalSerializer,
        responses={201: AnalyticalSerializer, 400: 'Bad Request'},
    )
    def post(self, request, *args, **kwargs):
        serializer = AnalyticalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnalyticalDetailView(APIView):
    parser_classes = [JSONParser]

    @swagger_auto_schema(
        operation_description="Get an analytical by ID",
        operation_summary="Get an analytical by ID",
        responses={200: AnalyticalSerializer, 404: 'Not Found'},
    )
    def get(self, request, pk, *args, **kwargs):
        try:
            analytical = Analytical.objects.get(pk=pk)
        except Analytical.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AnalyticalSerializer(analytical)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Update an analytical by ID",
        operation_summary="Update an analytical by ID",
        request_body=AnalyticalSerializer,
        responses={200: AnalyticalSerializer, 400: 'Bad Request', 404: 'Not Found'},
    )
    def put(self, request, pk, *args, **kwargs):
        try:
            analytical = Analytical.objects.get(pk=pk)
        except Analytical.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AnalyticalSerializer(analytical, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete an analytical by ID",
        operation_summary="Delete an analytical by ID",
        responses={204: 'No Content', 404: 'Not Found'},
    )
    def delete(self, request, pk, *args, **kwargs):
        try:
            analytical = Analytical.objects.get(pk=pk)
        except Analytical.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        analytical.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
