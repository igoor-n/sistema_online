from django.forms import ModelForm

from cadastro.models import Curso, Aluno, Professor


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


class ALunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

