from rest_framework import serializers 
from .models import song


class songserialzer(serializers.ModelSerializer):
    class Meta :
        model = song
        fields = "__all__"