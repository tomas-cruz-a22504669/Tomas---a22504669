"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('curso/', include('curso.urls')),
    path('', include('curso.urls')),  
    path('portfolio/', include('portfolio.urls')),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologia/nova/', views.nova_tecnologia_view, name='nova_tecnologia'),
    path('tecnologia/edita/<int:tecnologia_id>/', views.edita_tecnologia_view, name='edita_tecnologia'),
    path('tecnologia/apaga/<int:tecnologia_id>/', views.apaga_tecnologia_view, name='apaga_tecnologia'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('competencia/nova/', views.nova_competencia_view, name='nova_competencia'),
    path('competencia/edita/<int:competencia_id>/', views.edita_competencia_view, name='edita_competencia'),
    path('competencia/apaga/<int:competencia_id>/', views.apaga_competencia_view, name='apaga_competencia'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('formacao/nova/', views.nova_formacao_view, name='nova_formacao'),
    path('formacao/edita/<int:formacao_id>/', views.edita_formacao_view, name='edita_formacao'),
    path('formacao/apaga/<int:formacao_id>/', views.apaga_formacao_view, name='apaga_formacao'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
