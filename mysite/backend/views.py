# Imports
from .serializers import *
from .models import *
from rest_framework import viewsets,status
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication

# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('wallet', 'id')

# class ProfileLibraryViewSet(viewsets.ModelViewSet):
#     permission_classes=[AllowAny]
#     queryset=ProfileLibrary.objects.all()
#     serializer_class=ProfileLibrarySerializer
"""
class DomainViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=Domain.objects.all()
    serializer_class=DomainSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('profile', 'domain', 'id_contract')
    def create(self,request):
        data = request.data
        try:
            if data['seedPhrase'] and data['publicKey'] and data['secretKey']:
                serializer = self.get_serializer(data=data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                domain = Domain.objects.get(id=serializer.data['id'])
                DomainCredentials.objects.create(domain=domain.domain,seedPhrase=data['seedPhrase'],publicKey=data['publicKey'],secretKey=data['secretKey'])
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            return Response("Faltan datos",status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("%s"%(e),status=status.HTTP_400_BAD_REQUEST)
    #def list(self, request, *args, **kwargs):
    #    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    # def retrieve(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #def destroy(self, request, *args, **kwargs):
    #    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
"""      

class DomainCredentialsViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=DomainCredentials.objects.all()
    serializer_class=DomainCredentialsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id_contract','domain')
    #def create(self, request, *args, **kwargs):
    #    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #def list(self, request, *args, **kwargs):
    #    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #def retrieve(self, request, *args, **kwargs):
    #    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
"""
class PurchasedDomainViewSet(viewsets.ModelViewSet):
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[IsAdminUser]
    permission_classes=[AllowAny]
    queryset=PurchasedDomain.objects.all()
    serializer_class=PurchasedDomainSerializer
    def create(self,request):
        data = request.data
        try:
            if data['id'] and data['owner_id']:
                object = Domain.objects.get(id=data['id'], active=True)
                item = {
                    "id": data['id'],
                    "owner_id": data['owner_id'],
                    "domain": object.domain,
                    "price": object.price
                }
                serializer = self.get_serializer(data=item)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                object.delete()
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            return Response("Faltan datos",status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("%s"%(e),status=status.HTTP_400_BAD_REQUEST)
    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
"""
"""
class MarketViewSet(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    queryset=Domain.objects.filter(active=True)
    serializer_class=MarketSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('profile', 'domain', 'id_contract')
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #def list(self, request, *args, **kwargs):
    #    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    # def retrieve(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #def destroy(self, request, *args, **kwargs):
    #    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
"""

@api_view(["POST"])
@csrf_exempt
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def node_token(request):
    data = request.data
    if data['username'] == 'node' and data['password'] == 'node':
        usuario = User.objects.filter(username='node').first()
        token, create = Token.objects.get_or_create(user=usuario)
        print(token,create)
        return Response(token.key,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_403_FORBIDDEN)

 