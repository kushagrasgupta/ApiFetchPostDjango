from . models import userinfo
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = userinfo
        fields = '__all__'
        