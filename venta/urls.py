from django.urls import path
from . import views

urlpatterns = [
	path('',views.index),
	#Tabla de p vendidos
	path('vendido/', views.list_vendido),
	#CRUD Cliente
	path('cliente/',views.list_cliente),
	path('insert_cliente/',views.insert_cliente, name='insert_cli'),
	path('delete_cliente/<int:cli_id>/',views.delete_cliente, name='delete_cli'),
	path('search_cliente/', views.search_cli_nombre, name='search_cli'),#buscar cli x nom
	#CRUD Producto
	path('producto/',views.list_producto), #pag del producto
	path('insert_product/',views.insert_product, name='insert_prod'), #insertar un producto
	path('delete_product/<int:prod_id>/',views.delete_product, name='delete_prod'), #eliminar un producto
	#CRUD Vendedor
	path('vendedor/',views.list_vendedor),
	path('insert_vendedor/',views.insert_vendedor, name='insert_vendedor'),
	path('delete_vendedor/<int:vend_id>/',views.delete_vendedor, name='delete_vend'),
]