
from .models import Product
from rest_framework import generics
from .serializers import Productserilazers



class ProdactShome(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserilazers

class propk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserilazers


