from django.shortcuts import render, get_object_or_404
from .forms import FormServico
from django.http import HttpResponse, FileResponse
from .models import Servico
from fpdf import FPDF
from io import BytesIO
from django.shortcuts import redirect
from django.urls import reverse

#Função: Formulario add Serviços

def novo_servico(request):
    if request.method == "GET":
        form = FormServico()
        form.fields['categoria_manutencao'].widget.attrs['multiple'] = 'multiple'  # Adiciona o atributo 'multiple' ao widget
        return render(request, 'novo_servico.html', {'form': form})
    elif request.method == "POST":
        form = FormServico(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('listar_servico'))
        else:
            return render(request, 'novo_servico.html', {'form': form})
        
#Função: listagem de serviços

def listar_servico(request):
    if request.method == "GET":
        servicos = Servico.objects.all()
        return render(request, 'listar_servico.html', {'servicos': servicos})
    
#Função: Acessar serviço

def servico(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)
    return render(request, 'servico.html', {'servico': servico})

#Função: Mudar status do serviço

def finalizar_servico(request, identificador):
    servico = get_object_or_404(Servico, id=identificador)
    
    # Atualizar o campo 'finalizado' para True
    servico.finalizado = True
    servico.save()
    return redirect('listar_servico')


#Função: editar serviço

def editar_servico(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)

    if request.method == "POST":
        form = FormServico(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('servico', identificador=identificador)
    else:
        form = FormServico(instance=servico)

    return render(request, 'editar_servico.html', {'form': form})

#Função: Gerar OS

def gerar_os(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)
    
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 20)#fonte do Cabeçalho PDF
    pdf.set_fill_color(240,240,240)#Cor de fundo do cabeçalho
    pdf.cell(0, 30, 'Orçamento', 1, 1, 'C', 1)

    pdf.set_font('Arial', 'B', 13)#fonte do PDF

    pdf.set_fill_color(240,240,240)#Cor de fundo
    
    pdf.cell(0, 15, 'Leandro Cavalari Oficina' , 1, 1, 'L', 1)
    pdf.cell(0, 10, 'CNPJ: XX.XXX.XXX/XXXX-XX', 1, 1, 'L', 1)
    
    pdf.cell(40, 10, 'Cliente:', 1, 0, 'L', 1)#designer do PDF **ALTERAR
    pdf.cell(0, 10, f'{servico.cliente.nome}', 1, 1, 'L', 1)
    
    pdf.cell(40, 10, 'Manutenções:', 1, 0, 'L', 1)

    categorias_manutencao = servico.categoria_manutencao.all()
    for i, manutencao in enumerate(categorias_manutencao):
        preco_formatado = f'R${manutencao.preco:.2f}'  # Formata o preço com duas casas decimais
        pdf.cell(0, 10, f'- {manutencao.get_titulo_display()} ({preco_formatado})', 1, 1, 'L', 1)
        if not i == len(categorias_manutencao) - 1:
            pdf.cell(40, 10, '', 0, 0)

    # Adicionar descrição e observação se preenchidos

    descricao = servico.descricao
    observacao = servico.observacao

    if descricao:
        pdf.cell(40, 10, 'Descrição:', 1, 0, 'L', 1)
        pdf.multi_cell(0, 10, descricao, 1, 'L', 0)  # Quebra de linha automática

    if observacao:
        pdf.cell(40, 10, 'Observação:', 1, 0, 'L', 1)
        pdf.multi_cell(0, 10, observacao, 1, 'L', 0)

    pdf.cell(40, 10, 'Data de Inicio:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_inicio}', 1, 1, 'L', 1)
    pdf.cell(40, 10, 'Data de Entrega:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_entrega}', 1, 1, 'L', 1)
    pdf.cell(40, 10, 'Protocolo:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.identificador}', 1, 1, 'L', 1)
    pdf.cell(40, 10, 'Total:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.preco_total()}', 1, 0, 'L', 1)

    pdf_content = pdf.output(dest='S').encode('latin1')
    pdf_bytes = BytesIO(pdf_content)

    return FileResponse(pdf_bytes, as_attachment=True, filename=f"OS - {servico.identificador}.pdf")