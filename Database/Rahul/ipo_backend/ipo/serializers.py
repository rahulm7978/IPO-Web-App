from rest_framework import serializers
from .models import Company, IPO, Document, User, Application

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'