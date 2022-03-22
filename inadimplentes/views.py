from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from .models import Inquilino
from django.contrib import auth, messages


@csrf_exempt
def index(request):
    return redirect('login')

def pageinquilino(request, inquilino_id):
    inquilino = get_object_or_404(Inquilino, pk=inquilino_id)

    inquilino_a_exibir = {
        'inquilinos' : inquilino_id
    }

    return render(request, "pageinquilino.html", inquilino_a_exibir)

def buscar(request):
    lista_inquilinos = Inquilino.objects.order_by('-status_de_pagamentos').all()

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_inquilinos = lista_inquilinos.filter(nome__icontains=nome_a_buscar)
        
    dados = {
        'inquilinos' : lista_inquilinos
    }

    return render(request, 'buscar.html', dados)

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'O campo "Nome" não pode ficar em branco')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, 'O campo "E-mail" não pode ficar em branco')
            return redirect('cadastro')

        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais.')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, "Os campos e-mail ou senha não podem ficar em branco.")
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('inquilinos')
    messages.error(request, "Login ou senha inválido. Tente novamente")
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def inquilinos(request):
    inquilinos = Inquilino.objects.order_by('-status_de_pagamentos').all() # Exibindo totos inquilinos na ordem inversa
    
    dados = {
        'inquilinos' : inquilinos 
    }

    if request.user.is_authenticated:
        return render(request, 'inquilinos.html', dados)
    else:
        return redirect('login')

def cria_inquilino(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf  = request.POST['cpf']
        tamanho_do_kitnet  = request.POST['tamanho_do_kitnet']
        valor_do_aluguel  = request.POST['valor_do_aluguel']
        ultimo_pagamento  = request.POST['ultimo_pagamento']
        
        inquilino = Inquilino.objects.create(
        nome=nome,
        cpf=cpf,
        tamanho_do_kitnet=tamanho_do_kitnet,
        valor_do_aluguel=valor_do_aluguel,
        ultimo_pagamento=ultimo_pagamento)
        inquilino.save()
        return redirect('inquilinos')
    else:
        return render(request, 'usuarios/cadastro_inquilino.html')

def campo_vazio(campo):
    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2

