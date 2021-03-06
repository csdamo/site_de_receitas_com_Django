from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita


def cadastro(request):
    ''' Cadastra um novo usuário no sistema '''

    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'O campo e-mail não pode ficar em branco')
            return redirect('cadastro')
        if senhas_nao_sao_iguais(password, password2):
            messages.error(request, 'As senhas não conferem')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    ''' Realiza o login do usuário no sistema '''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['senha']
        if campo_vazio(email) or campo_vazio(password):
            messages.error(request, 'Os campos não pode ficar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=password)
            if user is not None:
                auth.login(request, user)
        return redirect('dashboard')
    return render(request, 'usuarios/login.html')


def logout(request):
    ''' Realiza o logout do usuário no sistema '''
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    ''' Mostra receitas do usuário na sua página quando ele está logado '''
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)

        dados = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')


def campo_vazio(campo):
    ''' retira os espaços para indicar se o campo está vazio '''
    return not campo.strip()


def senhas_nao_sao_iguais(password, password2):
    ''' Compara a senha com a senha de verificação '''
    return password != password2
