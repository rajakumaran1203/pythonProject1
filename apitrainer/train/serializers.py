from rest_framework import serializers
from .models import Employes
from uuid import uuid4
class Empserial(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255,required=False)
    email = serializers.EmailField(max_length=255, required=False,allow_null=False)
    job = serializers.CharField(max_length=255,required=False,allow_null=False)
    address=serializers.JSONField()
    class Meta:
        model=Employes
        fields=('name','email','job','address','is_active','is_delete')