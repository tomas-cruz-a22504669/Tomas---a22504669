import os
from django.core.files import File
from portfolio.models import Docente, Perfil, Projeto, Tecnologia, UnidadeCurricular
from curso.models import Curso

def migrar_modelo(modelo, campo_imagem):
    for obj in modelo.objects.all():
        imagem = getattr(obj, campo_imagem)
        if imagem and imagem.name:
            local_path = imagem.path
            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    imagem.save(os.path.basename(local_path), File(f), save=True)
                print(f"Migrado: {obj}")

# Executar para os teus modelos
print("A migrar Portfolio...")
migrar_modelo(Docente, 'fotografia')
migrar_modelo(Perfil, 'foto')
migrar_modelo(Projeto, 'imagem')
migrar_modelo(Tecnologia, 'logo')
migrar_modelo(UnidadeCurricular, 'imagem')

print("A migrar Curso...")
migrar_modelo(Curso, 'imagem')