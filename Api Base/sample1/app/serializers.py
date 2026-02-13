from rest_framework import serializers
from .models import*

# class StudentSerializer(serializers.Serializer):
#     roll =serializers.IntegerField()
#     name=serializers.CharField()
#     place=serializers.CharField()

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields='__all__'