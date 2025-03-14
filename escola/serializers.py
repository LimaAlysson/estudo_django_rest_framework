from rest_framework import serializers
from escola.models import Estudante, Curso

# Os serializers são utilizados para converter os models que são dados complexos em JSON

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__' #utilizando todos os campos de Curso