from rest_framework import serializers
from .models import HallMaster

class HallMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallMaster
        fields = '__all__'