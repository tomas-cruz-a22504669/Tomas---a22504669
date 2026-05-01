from django.urls import path
from . import views

urlpatterns = [
    path('registo/', views.registo_view, name='registo'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login/magico/', views.pedir_link_view, name='pedir_link'),
    path('login/magico/<str:token>/', views.login_magico_view, name='login_magico'),
]