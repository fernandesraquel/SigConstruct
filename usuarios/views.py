from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Funcionario, Usuario, Fornecedor, Cliente
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def homepage(request):
    return render(request, 'usuarios/homepage.html')


def sobre(request):
    return render(request, 'usuarios/sobre.html')


def cadastrar_gerente(request):
    if request.method == 'POST':
        username = request.POST['username']
        cpf = request.POST['cpf']
        remuneracao = request.POST['remuneracao']
        email = request.POST['email']
        senha = request.POST['password']
           
        usuario = Usuario.objects.filter(email=email)
        
        if usuario.exists():
            return HttpResponse('Email já existe')
        
        # Cria o usuário com cargo de gerente
        usuario = Usuario(
            username=username,
            password=make_password(senha),
            email=email,
            cargo='gerente',
            is_staff = True,
            is_superuser=True
        )
        usuario.save()
        
        # Cria funcionário associado ao usuário
        funcionario = Funcionario.objects.create(
            nome=username,
            cpf=cpf,
            remuneracao=remuneracao,
            email=email,
            usuario=usuario
        )      
        return redirect('logado')    
    return render(request, 'usuarios/cadastros/cadastro_gerente.html')


def cadastrar_vendedor(request):
    if request.method == 'POST':
        username = request.POST['username']
        cpf = request.POST['cpf']
        remuneracao = request.POST['remuneracao']
        email = request.POST['email']
        senha = request.POST['password']
           
        usuario = Usuario.objects.filter(email=email)
        
        if usuario.exists():
            return HttpResponse('Email já existe')
        
        # Cria o usuário com cargo de gerente
        usuario = Usuario(
            username=username,
            password=make_password(senha),
            email=email,
            cargo='vendedor',
        )
        usuario.save()
        
        # Cria funcionário associado ao usuário
        funcionario = Funcionario.objects.create(
            nome=username,
            cpf=cpf,
            remuneracao=remuneracao,
            email=email,
            usuario=usuario
        )      
        return redirect('homepage')
    return render(request, 'usuarios/cadastros/cadastro_vendedor.html')

def login_view(request):
    if request.method == 'POST':
        nome = request.POST['username']
        senha = request.POST['password']
        user = authenticate(request, username=nome, password=senha)
        if user is not None:
            login(request, user)
            return redirect('logado')
        else:
            messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
    return render(request, 'usuarios/registros/login.html')


def logado_view(request):
    return render(request, 'usuarios/registros/logado.html')


def logout_view(request):
    logout(request)
    return redirect('homepage')


def listar_funcionarios(request):
    funcionarios = Funcionario.objects.select_related('usuario').all()
    return render(request, 'usuarios/cadastros/listar_funcionarios.html', {'funcionarios': funcionarios})

def editar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)

    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        remuneracao = request.POST['remuneracao']
        email = request.POST['email']

        # Atualiza os dados do funcionário
        funcionario.nome = nome
        funcionario.cpf = cpf
        funcionario.remuneracao = remuneracao
        funcionario.email = email
        funcionario.save()

        return redirect('listar_funcionarios')
    
    return render(request, 'usuarios/cadastros/editar_funcionario.html', {'funcionario': funcionario})


def deletar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)

    if request.method == 'POST':
        # Remove o funcionário do banco de dados
        funcionario.delete()
        return redirect('listar_funcionarios')

    return render(request, 'usuarios/cadastros/deletar_funcionario.html', {'funcionario': funcionario})


def cadastro_funcionario(request, cargo):
    if request.method == 'POST':
        username = request.POST['username']
        cpf = request.POST['cpf']
        remuneracao = request.POST['remuneracao']
        email = request.POST['email']
        senha = request.POST['password']
        
        usuario = Usuario.objects.filter(email=email)
        
        if usuario.exists():
            return HttpResponse('Email já existe')
        
        if cargo == 'gerente':
            is_staff = True
            is_superuser = True
        else:
            is_staff = False
            is_superuser = False
        
        # Cria o usuário com o cargo específico
        usuario = Usuario(
            username=username,
            password=make_password(senha),
            email=email,
            cargo=cargo,
            is_staff=is_staff,
            is_superuser=is_superuser
        )
        usuario.save()
        
        # Cria o funcionário associado ao usuário
        funcionario = Funcionario.objects.create(
            nome=username,
            cpf=cpf,
            remuneracao=remuneracao,
            email=email,
            usuario=usuario
        )
        
        if cargo == 'gerente':
            return redirect('logado')
        else:
            return redirect('logado')
    
    if cargo == 'gerente':
        template_name = 'usuarios/cadastros/cadastro_gerente.html'
    else:
        template_name = 'usuarios/cadastros/cadastro_vendedor.html'
    
    return render(request, template_name)


def cadastrar_fornecedor(request):
    if request.method == 'POST':
    
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        cnpj = request.POST.get('cnpj')
        email = request.POST.get('email')
        
        fornecedor = Fornecedor(nome=nome, telefone=telefone,  cnpj=cnpj, email=email)
        fornecedor.save()
        
        return redirect('logado')

    elif request.method == 'GET':
        return render(request, 'fornecedor/cadastro_fornecedor.html')
    
def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()

    context = {'fornecedores': fornecedores}
    return render(request, 'fornecedor/listar_fornecedores.html', context)


def editar_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    if request.method == 'POST':
        # Extrair os dados do formulário
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')

        # Atualizar os dados do fornecedor
        fornecedor.nome = nome
        fornecedor.cnpj = cnpj
        fornecedor.telefone = telefone
        fornecedor.email = email
        fornecedor.save()

        return redirect('listar_fornecedores')
    else:
        # Preencher o formulário com os dados do fornecedor
        data = {
            'nome': fornecedor.nome,
            'cnpj': fornecedor.cnpj,
            'telefone': fornecedor.telefone,
            'email': fornecedor.email
        }

    # Passar os dados do fornecedor para o template
    context = {'form_data': data}
    return render(request, 'fornecedor/editar_fornecedor.html', context)


def deletar_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('listar_fornecedores')

    context = {'fornecedor': fornecedor}
    return render(request, 'fornecedor/deletar_fornecedor.html', context)