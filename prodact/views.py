from rest_framework.response import Response
from .models import Product
from rest_framework import generics,status
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from accounts.models import *
from accounts.serializers import ChateSerializer




class ProductManage(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["created_at"]
    search_fields = ["title", "category__name"]
    filterset_fields = ['title', "category"]




    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        return super(ProductManage, self).get_permissions()


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)


class MyProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)




class ChatUser(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        id_product = self.kwargs.get('id_product')
        return serializer.save(user=self.request.user,prodict_id=id_product)

class ListChat(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChateSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Chat.objects.filter(prodict__user=self.request.user)

