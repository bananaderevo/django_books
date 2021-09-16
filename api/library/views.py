from django.http import JsonResponse, Http404
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from .serializers import BooksSerializer, OrderSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Books, Order


class BookDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = get_object_or_404(Books, pk=pk)
        serializer = BooksSerializer(snippet, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BooksSerializer(snippet, data=request.data, context={'request': request})
        if serializer.is_valid() and self.request.user == snippet.author:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        if self.request.user == snippet.author:
            snippet.delete()
            return Response(status=204)
        return Response(status=400)


class BookList(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer