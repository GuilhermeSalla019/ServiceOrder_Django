from django.db.models import TextChoices

#Serviços prestados

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_OLEO_MOTOR = "TO", "Trocar de oleo"
    ALINHAMENTO_BALANCEAMENTO = "AB", "Alinhamento e Balanceamento"
    EMBREAGEM = "EM", "Manutenção/Troca na Embreagem"
    SISTEMA_FREIOS = "F", "Manutenção/Troca do Freio"
    TROCA_EM_GARANTIA = "TG", "Garantia Serviço/Troca"
    MANUTENÇÃO_SISTEMA_ARREFECIMENTO = "SA", "Manutenção no Sistema de Arrefecimento"
    TROCA_FILTRO = "TF", "Troca de Filtros"
    MANUTENCAO_SUSPENSAO = "S", "Manutenção/Troca na Suspensão"
    LIMPEZA_BICOS = "LB", "Limpeza de Bico"
    MANUTENCAO_MOTOR = "M", "Manutenção no Motor"
    TROCA_RADIADOR = "TR", "Troca do Radiador"
    TROCA_CORREIA_DENTADA = "TCD", "Troca da Correia Dentada"
    TROCA_MANGUEIRAS = "TM", "Troca de Mangueiras"
    TROCA_VELAS = "TV", "Troca das Velas"
    TROCA_PNEUS = "TP", "Troca de Pneus"
    OUTROS = "OS", "Outros Serviços"