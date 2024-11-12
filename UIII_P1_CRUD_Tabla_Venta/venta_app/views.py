from django.shortcuts import render, redirect
from .models import Venta

# Create your views here.

def Inicio_vista(request):
    lasventas=Venta.objects.all()
    return render(request, 'gestionarventa.html', {'misventas' : lasventas})

def RegistrarVenta(request):
    codigo=request.POST['txtcodigo']
    empaque=request.POST['txtempaque']
    contenido=request.POST['txtcontenido']
    dir_cliente=request.POST['txtdir_cliente']
    tel_cliente=request.POST['txttel_cliente']
    nom_cliente=request.POST['txtnom_cliente']
    total=request.POST['txttotal']

    guardarventas=Venta.objects.create(codigo=codigo, empaque=empaque, contenido=contenido, dir_cliente=dir_cliente,
                                        tel_cliente=tel_cliente, nom_cliente=nom_cliente, total=total)
    return redirect ("/")



def EditarVenta(request):
    codigo=request.POST['txtcodigo']
    empaque=request.POST['txtempaque']
    contenido=request.POST['txtcontenido']
    dir_cliente=request.POST['txtdir_cliente']
    tel_cliente=request.POST['txttel_cliente']
    nom_cliente=request.POST['txtnom_cliente']
    total=request.POST['txttotal']

    venta=Venta.objects.get(codigo=codigo)
    venta.empaque=empaque
    venta.contenido=contenido
    venta.dir_cliente=dir_cliente
    venta.tel_cliente=tel_cliente
    venta.nom_cliente=nom_cliente
    venta.total=total
    venta.save()
    return redirect ("/")

def SeleccionarVenta(request,codigo):
    venta=Venta.objects.get(codigo=codigo)
    return render(request,"EditarVenta.html",{"misventas":venta})

def BorrarVenta(request,codigo):
    venta=Venta.objects.get(codigo=codigo)
    venta.delete()
    return redirect("/")