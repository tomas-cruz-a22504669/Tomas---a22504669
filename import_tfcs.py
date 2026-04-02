import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import TFC

def carregar_dados():
    with open('data/tfcs_lusofona.json', encoding='utf-8') as f:
        dados = json.load(f)

    for item in dados:
        TFC.objects.create(
            titulo=item.get('titulo', ''),
            autores=item.get('autores', ''),
            orientadores=item.get('orientadores', ''),
            licenciaturas=item.get('licenciaturas', ''),
            ano=item.get('ano', ''),
            sumario=item.get('sumario', ''),
            pdf_link=item.get('pdf_link', ''),
            imagem=item.get('imagem', ''),
            rating=item.get('rating', 0)
        )
    print(f"Foram carregados {len(dados)} TFCs com sucesso!")

if __name__ == '__main__':
    carregar_dados()