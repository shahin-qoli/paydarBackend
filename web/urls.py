from web.views import AgentViewSet, InstallerViewSet
from django.urls import path, include

urlpatterns = [
    path('agents', AgentViewSet.as_view(), name= 'agents'),
    path('installers', InstallerViewSet.as_view(), name= 'installers')
]