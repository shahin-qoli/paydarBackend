from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from web.serializers import AgentSerializer,InstallerSerializer,CustomerSerializer,Installation
from web.models import Agent,Installer,Customer,Installation

# Create your views here.

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class InstallerViewSet(viewsets.ModelViewSet):
    queryset = Installer.objects.all()
    serializer_class = InstallerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = InstallerSerializer

class InstallerViewSet(viewsets.ModelViewSet):
    queryset = Installer.objects.all()
    serializer_class = InstallerSerializer
