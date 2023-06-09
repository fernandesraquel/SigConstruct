from django.urls import path
from .views import homepage, sobre, login_view, logado_view, logout_view, cadastro_funcionario
from .views import cadastrar_gerente, cadastrar_vendedor, listar_funcionarios, editar_funcionario, deletar_funcionario
from .views import cadastrar_fornecedor, listar_fornecedores, editar_fornecedor, deletar_fornecedor


urlpatterns = [
    path('', homepage, name='homepage'),
    path('sobre/', sobre, name='sobre'),
    path('login/', login_view, name='login'),
    path('logado/', logado_view, name='logado'), 
    path('logout/', logout_view, name='logout'),
    
    path('gerente/cadastrar', cadastrar_gerente, name='cadastrar_gerente'),
    path('vendedor/cadastrar', cadastrar_vendedor, name='cadastrar_vendedor'),
    path('funcionarios/listar', listar_funcionarios, name='listar_funcionarios'),
    path('funcionario/editar/<int:funcionario_id>/', editar_funcionario, name='editar_funcionario'),
    path('funcionario/deletar/<int:funcionario_id>/', deletar_funcionario, name='deletar_funcionario'),
    path('funcionarios/cadastrar/<str:cargo>/', cadastro_funcionario, name='cadastro_funcionario'),
    
    
    path('fornecedor/cadastrar', cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('fornecedores/listar', listar_fornecedores, name='listar_fornecedores'), 
    path('fornecedor/editar/<int:fornecedor_id>/', editar_fornecedor, name='editar_fornecedor'),
    path('fornecedor/deletar/<int:fornecedor_id>/', deletar_fornecedor, name='deletar_fornecedor'),
]
