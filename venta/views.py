from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import producto,cliente,vendedor
import logging
# Create your views here.

#PRODUCTOS VENDIDOS-------------------------------------------
def list_vendido(request):
	context = {'cliente_list' : cliente.objects.all().select_related("id_p")}
	return render(request,'venta/vendido.html',context)
#CLIENTES-----------------------------------------------------
def list_cliente(request):
	context = {'cliente_list' : cliente.objects.all()}
	return render(request,'venta/cliente.html',context)
def insert_cliente(request:HttpRequest):
	cli = cliente(
		nombre = request.POST['nombre'],
		apellido = request.POST['apellido'],
		correo = request.POST['correo'],
		telefono = request.POST['telefono'],
		direccion = request.POST['direccion'],
		id_p = producto.objects.get(id=int(request.POST['id_p']))
	)
	cli.save()
	return redirect('/venta/cliente/')
def delete_cliente(request, cli_id):
	eliminar_cliente = cliente.objects.get(id=cli_id)
	eliminar_cliente.delete()
	return redirect('/venta/cliente/')
def search_cli_nombre(request):
	context = {'cliente_list' : cliente.objects.filter(nombre = request.POST['nom'])}
	return render(request,'venta/cliente.html',context)
#PRODUCTOS----------------------------------------------------
#mostrar todos los productos
def list_producto(request):
	context = {'product_list' : producto.objects.all()}
	return render(request,'venta/producto.html',context)
#insertar productos
def insert_product(request:HttpRequest):
	prod = producto(
		nombre = request.POST['nombre'],
		marca = request.POST['marca'],
		categoria = request.POST['categoria'],
		fecha_v = request.POST['fecha_v']
	)
	prod.save()
	return redirect('/venta/producto/')
#eliminar productos
def delete_product(request, prod_id):
	eliminar_producto = producto.objects.get(id=prod_id)
	eliminar_producto.delete()
	return redirect('/venta/producto/')

#VENDEDORES---------------------------------------------------
def list_vendedor(request):
	context = {'vendedor_list' : vendedor.objects.all()}
	return render(request,'venta/vendedor.html',context)
def insert_vendedor(request:HttpRequest):
	vend = vendedor(
		nombre = request.POST['nombre'],
		apellido = request.POST['apellido'],
		dni = request.POST['dni']
	)
	vend.save()
	return redirect('/venta/vendedor/')
def delete_vendedor(request, vend_id):
	eliminar_vendedor = vendedor.objects.get(id=vend_id)
	eliminar_vendedor.delete()
	return redirect('/venta/vendedor/')