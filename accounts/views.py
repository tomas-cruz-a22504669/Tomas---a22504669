from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistoForm
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.models import User

def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistoForm()
    return render(request, 'accounts/registo.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def pedir_link_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            signer = TimestampSigner()
            token = signer.sign(user.username)
            link = request.build_absolute_uri(reverse('login_magico', args=[token]))
            
            send_mail(
                'O teu Link Mágico', 
                f'Clica aqui para entrar: {link}', 
                'admin@portfolio.com', 
                [email]
            )
            return render(request, 'accounts/link_enviado.html')
        except User.DoesNotExist:
            pass 
            
    return render(request, 'accounts/pedir_link.html')

def login_magico_view(request, token):
    signer = TimestampSigner()
    try:
        username = signer.unsign(token, max_age=900)
        user = User.objects.get(username=username)
        login(request, user)
        return redirect('projetos') 
    except (BadSignature, SignatureExpired, User.DoesNotExist):
        return render(request, 'accounts/link_invalido.html')    
