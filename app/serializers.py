from app.models import *
from rest_framework import serializers


class BirdsSeriallizer(serializers.ModelSerializer):
    class Meta:
        model=Birds
        fields=['username', 'bird_pic', 'bird_name', 'about']