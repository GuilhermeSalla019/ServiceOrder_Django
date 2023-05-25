from django.forms import ModelForm
from django import forms
from .models import Servico, CategoriaManutencao    

class FormServico(ModelForm):
    class Meta:
        model = Servico
        exclude = ['finalizado', 'protocole', 'identificador', ] #excluir campos do form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields['categoria_manutencao'].widget.attrs.update({'multiple': 'multiple'})
            self.fields[field].widget.attrs.update({'placeholder': field})

            self.fields['data_inicio'].widget.attrs.update({'placeholder': 'DD/MM/AAAA'})
            self.fields['data_entrega'].widget.attrs.update({'placeholder': 'DD/MM/AAAA'})

            #alterar descrição do serviço no form

        choices = list()
        for i, j in self.fields['categoria_manutencao'].choices:
            categoria = CategoriaManutencao.objects.get(titulo=j)
            choices.append((i.value, categoria.get_titulo_display()))

        self.fields['categoria_manutencao'].choices = choices