from rest_framework import serializers
from .models import Students,Groups


class GroupListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        fields = ['nameGroup', 'fact_count','day','aud']

class GroupCreateSerialzer(serializers.ModelSerializer):

    class Meta:
        fields = ['nameGroup', 'fact_count', 'day', 'aud']


class StudentsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['pk']

class StudentsCreateSerializer(serializers.ModelSerializer):
    def create(self,validated_data):
        return Students.objects.create(**validated_data)
    class Meta:
        model = Students
        fields = ['fio','group','subject','days']


