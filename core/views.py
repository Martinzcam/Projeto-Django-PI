from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm



def lista_projetos(request):
    projetos = Projeto.objects.all()

    return render(request, 'core/projetos/lista.html', {
        'projetos': projetos
    })


def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto cadastrado com sucesso!')
            return redirect('lista_projetos')
    else:
        form = ProjetoForm()

    return render(request, 'core/projetos/form.html', {
        'form': form,
        'titulo': 'Cadastrar Projeto'
    })


def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('lista_projetos')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'core/projetos/form.html', {
        'form': form,
        'titulo': 'Editar Projeto'
    })


def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto excluído com sucesso!')
        return redirect('lista_projetos')

    return render(request, 'core/projetos/confirmar_exclusao.html', {
        'projeto': projeto
    })

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()

    return render(request, 'core/tarefas/lista.html', {
        'tarefas': tarefas
    })


def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa cadastrada com sucesso!')
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()

    return render(request, 'core/tarefas/form.html', {
        'form': form,
        'titulo': 'Cadastrar Tarefa'
    })


def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)

        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'core/tarefas/form.html', {
        'form': form,
        'titulo': 'Editar Tarefa'
    })


def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('lista_tarefas')

    return render(request, 'core/tarefas/confirmar_exclusao.html', {
        'tarefa': tarefa
    })