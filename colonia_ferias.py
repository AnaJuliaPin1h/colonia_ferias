# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
# APLICATIVO: Sistema de Reservas - Colônia de Férias Corporativa
# DISCIPLINA: Software Básico
# DESCRIÇÃO:  Mini aplicativo para reserva de apartamentos na colônia de
#             férias da empresa, com cálculo automático do valor total.
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────

import os
import datetime

# ─────────────────────────────────────────────────────── CONSTANTES / BANCO DE DADOS EM MEMÓRIA ──────────────────────────────────
DIARIAS_TIPO1 = [20.00, 28.00, 35.00, 42.00, 48.00, 53.00]
DIARIAS_TIPO2 = [25.00, 34.00, 42.00, 50.00, 57.00, 63.00]

MAX_PESSOAS = 6
MAX_DIAS    = 7
MIN_DIAS    = 1
MIN_PESSOAS = 1

# ─────────────────────────────────────────────────────── FUNÇÕES AUXILIARES ───────────────────────────────────────────────────────

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_titulo():
    print("=" * 60)
    print("       SISTEMA DE RESERVAS")
    print("       Colônia de Férias Corporativa")
    print("=" * 60)


def linha_separadora(char="=", largura=60):
    print(char * largura)


def exibir_tabela_precos():
    print("\n  TABELA DE DIARIAS (R$ por pessoa)")
    linha_separadora("-", 52)
    print(f"  {'Pessoas':^10} {'Tipo 1 (R$)':^15} {'Tipo 2 (R$)':^15}")
    linha_separadora("-", 52)
    for i in range(MAX_PESSOAS):
        print(f"  {i+1:^10} R$ {DIARIAS_TIPO1[i]:>7.2f}     R$ {DIARIAS_TIPO2[i]:>7.2f}")
    linha_separadora("-", 52)


def ler_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"  Valor invalido! Informe um numero entre {minimo} e {maximo}.")
        except ValueError:
            print("  Entrada invalida! Por favor, digite apenas numeros inteiros.")


def ler_texto(mensagem, minimo=2, maximo=60):
    while True:
        texto = input(mensagem).strip()
        if minimo <= len(texto) <= maximo:
            return texto.title()
        else:
            print(f"  Nome invalido! Informe entre {minimo} e {maximo} caracteres.")


def calcular_valor(tipo_apto, num_pessoas, num_dias):
    indice = num_pessoas - 1

    if tipo_apto == 1:
        diaria_por_pessoa = DIARIAS_TIPO1[indice]
    else:
        diaria_por_pessoa = DIARIAS_TIPO2[indice]

    total_diaria = diaria_por_pessoa * num_pessoas
    valor_total  = total_diaria * num_dias

    return diaria_por_pessoa, total_diaria, valor_total


def emitir_relatorio(nome, tipo_apto, num_pessoas, num_dias,
                     diaria_pp, total_diaria, valor_total):
    agora = datetime.datetime.now()
    num_reserva = agora.strftime("%Y%m%d%H%M%S")

    print("\n")
    print("=" * 60)
    print(f"{'  COMPROVANTE DE RESERVA':^60}")
    print("=" * 60)

    print(f"  No. da Reserva  : {num_reserva}")
    print(f"  Data/Hora       : {agora.strftime('%d/%m/%Y  %H:%M:%S')}")
    linha_separadora("-", 60)

    print("\n  DADOS DO HOSPEDE")
    print(f"  Responsavel     : {nome}")

    print("\n  DETALHES DA RESERVA")
    print(f"  Tipo Apartamento: Tipo {tipo_apto}")
    print(f"  No. de Pessoas  : {num_pessoas} pessoa(s)")
    print(f"  Periodo         : {num_dias} dia(s)")

    print("\n  VALORES")
    print(f"  Diaria/pessoa   : R$ {diaria_pp:>8.2f}")
    print(f"  Total por dia   : R$ {diaria_pp:.2f} x {num_pessoas} pess. = R$ {total_diaria:>8.2f}")
    print(f"  Numero de dias  : R$ {total_diaria:.2f} x {num_dias} dias  = R$ {valor_total:>8.2f}")

    linha_separadora("=", 60)
    print(f"  VALOR TOTAL A PAGAR:  R$ {valor_total:,.2f}")
    linha_separadora("=", 60)

    print("\n  O pagamento devera ser efetuado na recepcao da colonia.")
    print("  Esta reserva e valida por 48 horas.\n")


def perguntar_nova_simulacao():
    while True:
        resposta = input("\n  Deseja fazer uma nova simulacao? [S/N]: ").strip().upper()
        if resposta in ('S', 'SIM', 'Y', 'YES'):
            return True
        elif resposta in ('N', 'NAO', 'NÃO', 'NO'):
            return False
        else:
            print("  Resposta invalida! Digite S para Sim ou N para Nao.")


# ─────────────────────────────────────────────────────── PROGRAMA PRINCIPAL ───────────────────────────────────────────────────────

def main():
    limpar_tela()
    exibir_titulo()

    print("  Bem-vindo(a) ao sistema de reservas da Colonia de Ferias!")
    print("  Preencha os dados abaixo para calcular o valor da sua reserva.")

    continuar = True
    while continuar:

        linha_separadora("=", 60)
        exibir_tabela_precos()
        linha_separadora("=", 60)

        print("\n  DADOS DA RESERVA\n")

        nome = ler_texto("  Nome do responsavel pela reserva: ")

        tipo_apto = ler_inteiro("  Tipo do apartamento [1 ou 2]: ", minimo=1, maximo=2)

        num_pessoas = ler_inteiro(
            f"  Numero de pessoas [1-{MAX_PESSOAS}]: ",
            minimo=MIN_PESSOAS, maximo=MAX_PESSOAS
        )

        num_dias = ler_inteiro(
            f"  Numero de dias [{MIN_DIAS}-{MAX_DIAS}]: ",
            minimo=MIN_DIAS, maximo=MAX_DIAS
        )

        diaria_pp, total_diaria, valor_total = calcular_valor(tipo_apto, num_pessoas, num_dias)

        emitir_relatorio(nome, tipo_apto, num_pessoas, num_dias,
                         diaria_pp, total_diaria, valor_total)

        continuar = perguntar_nova_simulacao()

        if continuar:
            limpar_tela()
            exibir_titulo()

    linha_separadora("=", 60)
    print("\n  Obrigado por usar o sistema de reservas!")
    print("  Boas ferias!\n")
    linha_separadora("=", 60)


if __name__ == "__main__":
    main()