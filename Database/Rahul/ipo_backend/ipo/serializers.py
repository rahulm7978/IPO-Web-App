from rest_framework import serializers
from .models import Company, IPO, Document

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class IPOSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = IPO
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    ipo = IPOSerializer(read_only=True)

    class Meta:
        model = Document
        fields = '__all__'
