import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import Licenciatura, UnidadeCurricular

def carregar_dados():
    pasta = 'files'
    for ficheiro in os.listdir(pasta):
        if ficheiro.endswith('-PT.json'):
            with open(os.path.join(pasta, ficheiro), encoding='utf-8') as f:
                dados = json.load(f)
            
            if 'curricularUnitName' in dados:
                curso, _ = Licenciatura.objects.get_or_create(
                    nome=dados.get('courseName', 'Desconhecido'),
                    defaults={'sigla': str(dados.get('courseCode', '')), 'grau': dados.get('diplomaDegree', ''), 'duracao_anos': 3, 'ects': 180}
                )
                UnidadeCurricular.objects.update_or_create(
                    codigo=dados.get('curricularIUnitReadableCode', ''),
                    defaults={'nome': dados.get('curricularUnitName', ''), 'ano_curricular': dados.get('curricularYear', 1), 'semestre': 1, 'ects': dados.get('ects', 0), 'descricao': dados.get('presentation', ''), 'licenciatura': curso}
                )
    print("Cursos e UCs carregados com sucesso!")

if __name__ == '__main__':
    carregar_dados()