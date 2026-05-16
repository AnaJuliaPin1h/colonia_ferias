from rest_framework import serializers
from .models import Reserva

PRECOS = {
    1: [20, 28, 35, 42, 48, 53],
    2: [25, 34, 42, 50, 57, 63],
}

class ReservaSerializer(serializers.ModelSerializer):
    valor_total = serializers.DecimalField(
        max_digits=8, decimal_places=2, read_only=True
    )

    class Meta:
        model = Reserva
        fields = '__all__'

    def validate_pessoas(self, value):
        if not 1 <= value <= 6:
            raise serializers.ValidationError('Número de pessoas deve ser entre 1 e 6.')
        return value

    def validate_dias(self, value):
        if not 1 <= value <= 7:
            raise serializers.ValidationError('Número de dias deve ser entre 1 e 7.')
        return value

    def create(self, validated_data):
        tipo = validated_data['tipo']
        pessoas = validated_data['pessoas']
        dias = validated_data['dias']
        preco_diaria = PRECOS[tipo][pessoas - 1]
        validated_data['valor_total'] = preco_diaria * dias
        return super().create(validated_data)