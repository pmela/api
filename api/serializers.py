from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aluno
        fields = ['url', 'id', 'nome', 'nascimento', 'filiacao', 'residencia']
