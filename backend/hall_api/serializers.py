from rest_framework import serializers
from .models import (
    User,
    HallMaster,
    SessionMaster,
    AdminMaster,
    Booking,
    Infrastructure,
    StatusDate,
    TimeSlot,
)

# ---------------------------
# User Serializer
# ---------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name']

# ---------------------------
# Hall Master Serializer
# ---------------------------
class HallMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallMaster
        fields = '__all__'

# ---------------------------
# Session Master Serializer
# ---------------------------
class SessionMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionMaster
        fields = '__all__'

# ---------------------------
# Admin Master Serializer
# ---------------------------
class AdminMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminMaster
        # Excluding password from direct API output for security
        exclude = ['password']

# ---------------------------
# Booking Serializer
# ---------------------------
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

# ---------------------------
# Infrastructure Serializer
# ---------------------------
class InfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infrastructure
        fields = '__all__'

# ---------------------------
# StatusDate Serializer
# ---------------------------
class StatusDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusDate
        fields = '__all__'

# ---------------------------
# TimeSlot Serializer
# ---------------------------
class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'
