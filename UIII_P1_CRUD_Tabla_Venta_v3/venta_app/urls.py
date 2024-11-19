from django.urls import path
from venta_app import views

urlpatterns = [
    path('', views.Inicio_vista, name='inicio'),
    path('registrarVenta/', views.RegistrarVenta, name='registrar_venta'),
    path('editarVenta/', views.editarVenta, name='editar_venta'),
    path('seleccionarVenta/<int:codigo>/', views.SeleccionarVenta, name='seleccionar_venta'),
    path('borrarVenta/<int:codigo>/', views.BorrarVenta, name='borrar_venta'),
]
