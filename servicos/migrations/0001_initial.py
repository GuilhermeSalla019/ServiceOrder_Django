# Generated by Django 4.1.7 on 2023-04-11 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0002_alter_carro_placa'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaManutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(choices=[('TO', 'Trocar de oleo'), ('AB', 'Alinhamento e Balanceamento'), ('EM', 'Manutenção/Troca na Embreagem'), ('F', 'Manutenção/Troca do Freio'), ('TG', 'Garantia Serviço/Troca'), ('SA', 'Manutenção no Sistema de Arrefecimento'), ('TF', 'Troca de Filtros'), ('S', 'Manutenção/Troca na Suspensão'), ('LB', 'Limpeza de Bico'), ('M', 'Manutenção no Motor'), ('TR', 'Troca do Radiador'), ('TCD', 'Troca da Correia Dentada'), ('TM', 'Troca de Mangueiras'), ('TV', 'Troca das Velas'), ('TP', 'Troca de Pneus'), ('OS', 'Outros Serviços')], max_length=3)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('data_inicio', models.DateField(null=True)),
                ('data_entrega', models.DateField(null=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('protocole', models.CharField(blank=True, max_length=52, null=True)),
                ('categoria_manutencao', models.ManyToManyField(to='servicos.categoriamanutencao')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.cliente')),
            ],
        ),
    ]
