from rest_framework.serializers import ModelSerializer
from .models import Project, Measurement


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = 'id', 'name', 'latitude', 'longitude'


class MeasurementSerializer(ModelSerializer):
    class Meta:
        model = Measurement
        fields = 'id', 'value', 'project', 'image'
