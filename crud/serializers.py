"""
Here live the serializers for this app's models
"""

from .models import Company, Software
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ["url", "name", "score"]


class SoftwareSerializer(serializers.HyperlinkedModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), write_only=True
    )

    class Meta:
        model = Software
        fields = ["url", "name", "trust_score", "company"]
