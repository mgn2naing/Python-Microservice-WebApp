from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer
from rest_framework.response import Response
class ProductViewSet(viewsets.ViewSet):

    def list(self, request): #/api/product/
        product = Product.objects.all()
        serializer = ProductSerializer(product, Many=True)
        return Response(serializer.data)


    def create(self, request): #/api/product/
        pass

    def retrive(self, request, pk=None): #/api/product/<str:id>
        pass

    def update(self, request, pk=None): #/api/product/<str:id>
        pass

    def destroy(self, request, pk=None):
        pass


# Create your views here.
