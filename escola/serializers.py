from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula

# Os serializers são utilizados para converter os models que são dados complexos em JSON

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve ter 11 digitos!')
        return cpf

    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError('O nome deve conter apenas letras!')
        return nome

    def validate_celular(self, celular):
        if len(celular) != 13:
            raise serializers.ValidationError('O celular deve ter 13 dígitos!')
        return celular

    def validate(self, dados):
        if len(dados['cpf']) != 11:
            raise serializers.ValidationError({'cpf':'O CPF deve ter 11 digitos!'})
        if not dados['nome'].isalpha():
            raise serializers.ValidationError({'nome':'O nome deve conter apenas letras!'})
        if len(dados['celular']) != 13:
            raise serializers.ValidationError({'celular':'O celular deve ter 13 dígitos!'})
        return dados

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__' #utilizando todos os campos de Curso

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']