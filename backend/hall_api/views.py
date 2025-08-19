from rest_framework import viewsets
from .models import HallMaster
from .serializers import HallMasterSerializer

class HallMasterViewSet(viewsets.ModelViewSet):
    queryset = HallMaster.objects.all()
    serializer_class = HallMasterSerializer
