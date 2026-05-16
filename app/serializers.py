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
    total = serializers.DecimalField(   # ← alias para o JS
        max_digits=8, decimal_places=2, read_only=True, source='valor_total'
    )

    class Meta:
        model  = Reserva
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
        tipo    = validated_data['tipo']
        pessoas = validated_data['pessoas']
        dias    = validated_data['dias']
        validated_data['valor_total'] = PRECOS[tipo][pessoas - 1] * dias
        return super().create(validated_data)

    def update(self, instance, validated_data):
        tipo    = validated_data.get('tipo', instance.tipo)
        pessoas = validated_data.get('pessoas', instance.pessoas)
        dias    = validated_data.get('dias', instance.dias)
        validated_data['valor_total'] = PRECOS[tipo][pessoas - 1] * dias
        return super().update(instance, validated_data)