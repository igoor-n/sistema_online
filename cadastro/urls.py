from django.urls import path

from cadastro import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teste', views.teste, name='teste'),
    path('print', views.print_em_html, name='print'),

    path('listar_curso', views.listarCursos, name='listarCurso'),
    path('incluir_curso', views.incluirCurso,
         name='incluirCurso'),
    path('editar_curso/<int:id>', views.editarCurso, name='editarCurso'),
    path('excluir_curso/<int:id>', views.excluirCurso, name='excluirCurso'),

    path('listar_alunos', views.listarAlunos, name='listarAlunos'),
    path('incluirAluno', views.incluirAluno, name='incluirAluno'),
    path('editarAluno/<int:id>', views.editarAluno, name='editarAluno'),
    path('excluirAluno/<int:id>', views.excluirAluno, name='excluirAluno'),

    path('listar_professores', views.listarProfessores, name='listarProfessores'),
    path('incluirProfessores', views.incluirProfessores, name='incluirProfessores'),
    path('editarProfessores/<int:id>', views.editarProfessores, name='editarProfessores'),
    path('excluirProfessores/<int:id>', views.excluirProfessores, name='excluirProfessores')

]