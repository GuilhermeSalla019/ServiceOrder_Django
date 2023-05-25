from django.db.models import TextChoices

#Serviços prestados

class ChoicesCategoriaManutencao(TextChoices):
    ALINHAMENTO_BALANCEAMENTO = "AB", "Alinhamento e Balanceamento"
    AR_CONDICIONADOS = "AC", "Ar Condicionado"
    DIAGNÓSTICO_PROBLEMA = "DP", "Diagnostico de Problemas"
    EMBREAGEM = "EM", "Manutenção/Troca na Embreagem"
    LIMPEZA_BICOS = "LB", "Limpeza de Bico"
    MANUTENCAO_SUSPENSAO = "S", "Manutenção/Troca na Suspensão"
    MANUTENCAO_MOTOR = "M", "Manutenção no Motor"
    MANUTENÇÃO_SISTEMA_ARREFECIMENTO = "SA", "Manutenção no Sistema de Arrefecimento"
    SISTEMA_FREIOS = "F", "Manutenção/Troca do Freio"
    SISTEMA_IGNICAO = "SI", "Sistema de Ignição"
    SISTEMA_ESCAPE = "SE", "Sistema de Escape"
    SERVIÇOS_ELETRICOS = "SEL", "Serviços Elétricos"
    SERVIÇOS_TRANSMISSÃO = "ST", "Serviços de Transmissão"
    TROCA_BATERIA = "TB", "Troca de Bateria"
    TROCA_EM_GARANTIA = "TG", "Garantia Serviço/Troca"
    TROCA_FILTRO = "TF", "Troca de Filtros"
    TROCAR_OLEO_MOTOR = "TO", "Trocar de oleo"
    TROCA_RADIADOR = "TR", "Troca do Radiador"
    TROCA_CORREIA_DENTADA = "TCD", "Troca da Correia Dentada"
    TROCA_MANGUEIRAS = "TM", "Troca de Mangueiras"
    TROCA_VELAS = "TV", "Troca das Velas"
    TROCA_PNEUS = "TP", "Troca de Pneus"
    OUTROS = "OS", "Outros Serviços"