from rest_framework import serializers
from web.models import Agent,Installer,Customer,Installation
import abc

class BaseSerializer(serializers.ModelSerializer,metaclass=abc.ABCMeta):
    class Meta:
        fields = '__all__'
        model = None

class AgentSerializer(BaseSerializer):
    class Meta:
        model = Agent

class InstallerSerializer(BaseSerializer):
    class Meta:
        model = Installer

class CustomerSerializer(BaseSerializer):
    class Meta:
        model = Customer

class InstallationSerializer(BaseSerializer):
    class Meta:
        model = Installation