from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Webtoon
from .serializers import WebtoonSerializer

class WebtoonViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        webtoons = Webtoon.objects.all()
        serializer = WebtoonSerializer(webtoons, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            webtoon = Webtoon.objects.get(pk=pk)
            serializer = WebtoonSerializer(webtoon)
            return Response(serializer.data)
        except Webtoon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = WebtoonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            webtoon = Webtoon.objects.get(pk=pk)
            webtoon.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Webtoon.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
