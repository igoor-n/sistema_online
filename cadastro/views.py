from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from cadastro.forms import CursoForm, ALunoForm, ProfessorForm
from cadastro.models import Curso, Aluno, Professor


# Create your views here.

def index(request):
    return render(request, "início.html")


def teste(request):
    return HttpResponse("Isso é um teste.")

def print_em_html(request):
    return HttpResponse("<h2>Um título</h2>")

def listarCursos(request):
    cursos = Curso.objects.all().order_by('nome')
    return render(request, "listar_cursos.html",
                  {'lista':cursos})

def incluirCurso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model= form.instance
                return redirect('listarCurso')
            except:
                pass
    else:
        form = CursoForm()

    return render(request, "incluir_curso.html",
                  {'form': form})

def editarCurso(request,id):
    curso = Curso.objects.get(codigo=id)
    form = CursoForm(instance=curso)

    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            try:
                form.save()
                return redirect('listarCurso')
            except:
                pass


    return render(request, "incluir_curso.html",
                  {'form': form})

def excluirCurso(request, id):
    curso = Curso.objects.get(codigo=id)
    try:
        curso.delete()
    except:
        messages.error(request, "Não é possível excluir.")
    return redirect('listarCurso')


def listarAlunos(request):
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, "listar_alunos.html",
                  {'lista': alunos})





def incluirAluno(request):
    if request.method == 'POST':
        form = ALunoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('listarAlunos')
            except:
                pass
    else:
        form = CursoForm()

    return render(request, "incluir_aluno.html",
                  {'form': form})


def editarAluno(request, id):
    aluno = Aluno.objects.get(codigo=id)
    form = ALunoForm(instance=aluno)

    if request.method == "POST":
        form = CursoForm(request.POST, instance=aluno)
        if form.is_valid():
            try:
                form.save()
                return redirect('listarAlunos')
            except:
                pass


def excluirAluno(request,id):
    aluno = Aluno.objects.get(codigo=id)
    try:
        Aluno.delete()
    except:
        messages.error(request, "Não é possível excluir.")
    return redirect('listarAluno')


def listarProfessores(request):
    professores = Professor.objects.all().order_by('nome')
    return render(request, "listar_professores.html",
                  {'lista': professores})


def incluirProfessores(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('listarProfessores')
            except:
                pass
    else:
        form = CursoForm()

    return render(request, "incluir_professores.html",
                  {'form': form})


def editarProfessores(request, id):
    professor = Professor.objects.get(codigo=id)
    form = ALunoForm(instance=professor)

    if request.method == "POST":
        form = CursoForm(request.POST, instance=professor)
        if form.is_valid():
            try:
                form.save()
                return redirect('listarProfessores')
            except:
                pass


def excluirProfessores(request, id):
    professor = Professor.objects.get(codigo=id)
    try:
        Professor.delete()
    except:
        messages.error(request, "Não é possível excluir.")
    return redirect('listarProfessores')