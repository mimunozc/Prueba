#from django.conf.urls import url
from django.urls import path, include
from  . import views 



urlpatterns=[
    path("index", views.index, name="index"),
    path("flores", views.flores_crud, name="flores" ),
    path("maceteros",views.maceteros_crud, name="maceteros"),
    path("tierra",views.tierra_crud, name="tierra"),
    path("seguimiento",views.seguimiento_crud, name="seguimiento"),
    path("carro",views.carro_crud, name="carro"),
    path('desc/<str:pk>',views.desc, name='desc'),
    

    #Registro , login
    path("salir/",views.salir, name="salir"),
    path("loguear",views.login_request,name="loguear"),
    path("registro",views.register_request, name="register_request"),
    path("logout", views.logout_request, name= "logout_request"),
    

    #productos
    path("administrador",views.admin_crud, name="administrador"),
    path("productos",views.productos_crud, name="productos_crud"),
    path("productosAdd",views.productosAdd,name="productosAdd"),
    path('productos_del/<str:pk>', views.productos_del, name='productos_del'),
    path('productos_edit/<str:pk>', views.productos_edit, name='productos_edit'),

    #personas
    path("personas",views.personas_crud, name="personas"),
    path("personasAdd",views.personasAdd,name="personasAdd"),
    path('personas_del/<str:pk>', views.personas_del, name='personas_del'),
    path('personas_edit/<str:pk>', views.personas_edit, name='personas_edit'),

    #carrito 

    path('agregar/<str:producto_id>', views.agregar_producto, name="agregar"),
    path('agregar_flores/<str:producto_id>', views.agregar_producto2, name="agregar_flores"),
    path('eliminar/<str:producto_id>', views.eliminar_producto, name="eliminar"),
    path('restar/<str:producto_id>', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carro, name='limpiar'),
    path('pedido/', views.procesar_pedido, name='pedido'),

    
]