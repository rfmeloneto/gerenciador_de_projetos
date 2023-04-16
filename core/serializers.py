from rest_framework import serializers
from .models import User, Project

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'email']
        
class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'users']
        
class AssociateSerializer(serializers.Serializer):
    project_id = serializers.IntegerField()


class DisassociateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

