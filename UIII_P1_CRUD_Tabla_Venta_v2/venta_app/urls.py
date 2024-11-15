from django.urls import path
from venta_app import views

urlpatterns = [
    path('', views.Inicio_vista, name='Inicio_vista'),
    path('RegistrarVenta/' ,views.RegistrarVenta, name='RegistrarVenta' ),
    path("SeleccionarVenta/<codigo>",views.SeleccionarVenta,name="SeleccionarVenta"),
    path("EditarVenta/",views.EditarVenta,name="EditarVenta"),
    path("BorrarVenta/<codigo>",views.BorrarVenta,name="BorrarVenta")
]