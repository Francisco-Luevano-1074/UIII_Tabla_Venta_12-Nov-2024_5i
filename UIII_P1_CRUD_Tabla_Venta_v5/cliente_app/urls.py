from django.urls import path
from cliente_app import views

urlpatterns = [
    path('', views.Inicio_oido, name='inicio'),
    path('registrarCliente/', views.RegistrarCliente, name='registrar_cliente'),
    path('editarCliente/', views.editarCliente, name='editar_cliente'),
    path('seleccionarCliente/<int:codigo>/', views.SeleccionarCliente, name='seleccionar_cliente'),
    path('borrarCliente/<int:codigo>/', views.BorrarCliente, name='borrar_cliente'),
]
