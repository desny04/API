from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    roll =serializers.IntegerField()
    name=serializers.CharField()
    place=serializers.CharField()