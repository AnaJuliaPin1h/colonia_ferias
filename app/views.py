from django.shortcuts import render
from django.http import HttpResponse

from reportlab.pdfgen import canvas
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Reserva
from .serializers import ReservaSerializer

DIARIAS_TIPO1 = [20, 28, 35, 42, 48, 53]
DIARIAS_TIPO2 = [25, 34, 42, 50, 57, 63]

def calcular_diaria(tipo, pessoas):
    """Centraliza o cálculo para não repetir código."""
    tabela = DIARIAS_TIPO1 if tipo == 1 else DIARIAS_TIPO2
    return tabela[pessoas - 1]


def index(request):
    resultado = None

    if request.method == "POST":
        nome    = request.POST["nome"]
        tipo    = int(request.POST["tipo"])
        pessoas = int(request.POST["pessoas"])
        dias    = int(request.POST["dias"])

        diaria = calcular_diaria(tipo, pessoas)
        total  = diaria * dias

        resultado = Reserva.objects.create(
            nome=nome,
            tipo=tipo,
            pessoas=pessoas,
            dias=dias,
            valor_total=total,
        )

    return render(request, "index.html", {"resultado": resultado})


def gerar_pdf(request, id):
    reserva = Reserva.objects.get(id=id)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="reserva.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 800, "COMPROVANTE DE RESERVA")
    p.drawString(100, 780, f"Nome: {reserva.nome}")
    p.drawString(100, 760, f"Tipo: {reserva.get_tipo_display()}")
    p.drawString(100, 740, f"Pessoas: {reserva.pessoas}")
    p.drawString(100, 720, f"Dias: {reserva.dias}")
    p.drawString(100, 700, f"Total: R$ {reserva.valor_total}")
    p.showPage()
    p.save()

    return response


class ReservaViewSet(viewsets.ModelViewSet):
    queryset         = Reserva.objects.all().order_by('-criado_em')
    serializer_class = ReservaSerializer

    def create(self, request, *args, **kwargs):
        dados   = request.data
        tipo    = int(dados.get('tipo', 1))
        pessoas = int(dados.get('pessoas', 1))
        dias    = int(dados.get('dias', 1))
        nome    = dados.get('nome', '')

        # Validações básicas
        if not nome:
            return Response({'erro': 'Nome é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)
        if not (1 <= pessoas <= 6):
            return Response({'erro': 'Número de pessoas deve ser entre 1 e 6.'}, status=status.HTTP_400_BAD_REQUEST)
        if not (1 <= dias <= 7):
            return Response({'erro': 'Número de dias deve ser entre 1 e 7.'}, status=status.HTTP_400_BAD_REQUEST)

        diaria = calcular_diaria(tipo, pessoas)
        total  = diaria * dias

        reserva = Reserva.objects.create(
            nome=nome,
            tipo=tipo,
            pessoas=pessoas,
            dias=dias,
            valor_total=total,
        )

        return Response({
            'id':      reserva.id,
            'nome':    reserva.nome,
            'tipo':    reserva.tipo,
            'pessoas': reserva.pessoas,
            'dias':    reserva.dias,
            'total':   reserva.valor_total,   # ← o JS usa esse campo
        }, status=status.HTTP_201_CREATED)