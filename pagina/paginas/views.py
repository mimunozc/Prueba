from dataclasses import dataclass
from multiprocessing import context
from django.shortcuts import redirect, render
from django.urls import is_valid_path


from .models import  DetalleVenta, Personas, Producto, Venta
from django.contrib.auth.models import User
from .carrito import Carrito
from .forms import UserRegisterForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib.auth import logout ,authenticate ,login
from django.contrib.auth.forms import AuthenticationForm





# Create your views here.


def index(request):
    print("Hola estoy en index....")
    context={}
    return render (request,'paginas/index.html',context)

def salir(request):
    logout(request)
    return redirect('index')
    # Redirect to a success page.

def flores_crud(request):
    print("Hola estoy en flores")
    productos = Producto.objects.all()
    context={'productos':productos}
    opcion=request.POST.get("opcion","")
    if  opcion == "Volver":
            print("enviando datos a productos_list")
            return render(request,"paginas/flores.html",context)
    return render(request,'paginas/flores.html', context)

def flor_1(request):
    print("Hola estoy en flor1....")
    context={}
    return render (request,'paginas/flores.html',context)

def maceteros_crud(request):
    print("Hola estoy en maceteros")
    context={}
    return render(request,'paginas/maceteros.html', context)

def tierra_crud(request):
    print("Hola estoy en tierra")
    context={}
    return render(request,'paginas/tierra.html', context)

def seguimiento_crud(request):
    print("Hola estoy en seguimiento")
    context={}
    return render(request,'paginas/seguimiento.html', context)

def login_crud(request):
    print("Hola estoy en login")
    context={}
    if request.method == "POST":
        form = login_crud
    return render(request,"paginas/logina.html", context)

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			Contraseña = form.cleaned_data.get('password')
			user = authenticate(username=username, password=Contraseña)
			if user is not None:
				login(request, user)
				messages.info(request, f"Estas logueado como {username}.")
				return redirect('index')
			else:
				messages.error(request,"Usuario o Contraseña invalido.")
		else:
			messages.error(request,"Usuario o Contraseña invalido")
	form = AuthenticationForm()
	return render(request=request, template_name='paginas/loguear.html', context={"login_form":form})

def registro_crud(request):
    print("Hola estoy en registro")
    context ={}
    return render(request,'paginas/registro.html', context)

def register_request(request):
    print("Hola estoy en registro")
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Usuario Registrado.")
            return redirect('index')
        messages.error(request,"Error , no se realizo el registro")
    form = UserRegisterForm()
    return render(request=request,template_name='paginas/registros.html',context={"register_form":form})



def logout_request(request):
	logout(request)
	messages.success(request, "Te has deslogueado correctamente") 
	return redirect("index")


def carro_crud(request):
    print("Hola estoy en carro")
    context={}
    return render(request,'paginas/carro.html', context)


def admin_crud(request):
    print("Hola estoy en admin")
    context={}
    return render(request,'paginas/base_admin.html', context)


def productos_crud(request):
    print("Hola estoy en productos")
    context={}
    return render(request,'paginas/productos_add.html', context)


def producto_edit(request):
    print("Hola estoy en productos Edit")
    context={}
    return render(request,'paginas/productos_edit.html', context)


def desc_list(request):
    context={}
    return render(request,'paginas/desc.html',context)

def desc(request,pk):
    print("Hola estoy en productos Edit")
    
    productos=Producto.objects.get(idProducto=pk)
    if productos:
    
        print("Edit encontró a producto...")
        

        context = {'producto': productos}

        return render(request, 'paginas/desc.html', context)
    
    


    


##################   P R O D U C T O S ######################

def productosAdd(request):
    print("estoy en controlador ProductosAdd...")
    context={}
    if request.method == "POST":
        print("contralador productos es un post...") 
        opcion=request.POST.get("opcion","")
        print("opcion="+opcion)
        #Listar
        if opcion=="Editar" or opcion == "Volver":
            productos = Producto.objects.all()
            context ={'productos':productos}
            print("enviando datos a productos_list")
            return render(request,"paginas/productos_list.html",context) 
        #Agregar
        if opcion=="Agregar":
            idProducto=request.POST["idProducto"]
            marcaProducto=request.POST["marcaProducto"]
            nombreProducto=request.POST["nombreProducto"]
            stock=int(request.POST["stock"])
            precio=int(request.POST["precio"])
            try:
                fotoProducto=request.FILES["fotoProducto"]
            except:
                fotoProducto=""
            

       
            if idProducto != "" and marcaProducto !="" and nombreProducto != "" and stock >=0 and precio >=0:

                producto = Producto(idProducto, marcaProducto,nombreProducto, stock, precio,
                                    fotoProducto) 
                producto.save()
                context={'mensaje':"Ok, datos grabados..."}
            else:
                context={'mensaje':"Error, los campos no deben estar vacios"}

           #Agregar
        if opcion=="Actualizar":
            idProducto=request.POST["idProducto"] 
            marcaProducto=request.POST["marcaProducto"]
            nombreProducto=request.POST["nombreProducto"]
            stock=int(request.POST["stock"])
            precio=int(request.POST["precio"])
            try:
                fotoProducto=request.FILES["fotoProducto"]
            except:
                fotoProducto=""
       
            if idProducto != "" and marcaProducto !="" and nombreProducto != "" and stock >=0 \
                and precio >=0:

                producto = Producto(idProducto,marcaProducto,nombreProducto, stock, precio,
                                    fotoProducto) 
                producto.save()
                context={'mensaje':"Ok, datos grabados..."}
            else:
                context={'mensaje':"Error, los campos no deben estar vacios"}
            return render(request,"paginas/productos_edit.html",context) 


    return render(request,"paginas/productos_add.html",context)



def productos_del(request, pk):
    mensajes=[]
    errores=[]
    productos = Producto.objects.all()
    try:
        producto=Producto.objects.get(idProducto=pk)
        context={}
        if producto:
           producto.delete()
           mensajes.append("Bien, datos eliminados...")

           context = {'productos': productos,  'mensajes': mensajes, 'errores':errores}

           return render(request, 'paginas/productos_list.html', context)

    except:
        print("Error, rut no existe")
        errores.append("Error rut no encontrado.")
        context = {'productos': productos,  'mensajes': mensajes, 'errores':errores}
        return render(request, 'paginas/productos_list.html', context)


def productos_edit(request, pk):
    mensajes=[]
    errores=[]   
    
    context={}
    #productos = Producto.objects.all()
    #try:
    producto=Producto.objects.get(idProducto=pk)

    context={}
    if producto:
        print("Edit encontró a producto...")
        mensajes.append("Bien, datos eliminados...")

        context = {'producto': producto,  'mensajes': mensajes, 'errores':errores}

        return render(request, 'paginas/productos_edit.html', context)
    
    return render(request, 'paginas/productos_list.html', context)
    
##################   PERSONAS   ########################


def personas_crud(request):
    print("Hola estoy en personas")
    context={}
    return render(request,'paginas/personas_add.html', context)


def personasAdd(request):
    print("estoy en controlador PersonasAdd...")
    context={}
    if request.method == "POST":
        print("contralador personas es un post...") 
        opcion=request.POST.get("opcion","")
        print("opcion="+opcion)
        #Listar
        if opcion=="Editar" or opcion == "Volver":
            personas = Personas.objects.all()
            context ={'personas':personas}
            print("enviando datos a personas_list")
            return render(request,"paginas/personas_list.html",context) 
        #Agregar
        if opcion=="Agregar":
            idPersona=request.POST["idPersona"]
            nombrePersona=request.POST["nombrePersona"]
            usuario=request.POST["usuario"]
            email=request.POST["email"]
            contrasena=request.POST["contrasena"]
            tipoUsuario=request.POST["tipoUsuario"]

            try:
                fotoPersona=request.FILES["fotoPersona"]
            except:
                fotoPersona=""

       
            if idPersona != "" and nombrePersona !="" and usuario != "" and email !="" and contrasena !="" and tipoUsuario !="":

                persona = Personas(idPersona, nombrePersona,usuario, email,contrasena,tipoUsuario,
                                    fotoPersona) 
                persona.save()
                context={'mensaje':"Ok, datos grabados..."}
            else:
                context={'mensaje':"Error, los campos no deben estar vacios"}

           #Agregar
        if opcion=="Actualizar":
            idPersona=request.POST["idPersona"]
            nombrePersona=request.POST["nombrePersona"]
            usuario=request.POST["usuario"]
            email=request.POST["email"]
            contrasena=request.POST["contrasena"]
            tipoUsuario=request.POST["tipoUsuario"]

            try:
                fotoPersona=request.FILES["fotoPersona"]
            except:
                fotoPersona=""
       
            if idPersona != "" and nombrePersona !="" and usuario != "" and email !="" and contrasena !="" and tipoUsuario !="":

                persona = Personas(idPersona, nombrePersona,usuario, email,contrasena,tipoUsuario,
                                    fotoPersona)  
                persona.save()
                context={'mensaje':"Ok, datos grabados..."}
            else:
                context={'mensaje':"Error, los campos no deben estar vacios"}
            return render(request,"paginas/personas_edit.html",context) 


    return render(request,"paginas/personas_add.html",context)

    
def personas_del(request, pk):
    mensajes=[]
    errores=[]
    personas = Personas.objects.all()
    try:
        persona=Personas.objects.get(idPersona=pk)
        context={}
        if persona:
           persona.delete()
           mensajes.append("Bien, datos eliminados...")

           context = {'personas': personas,  'mensajes': mensajes, 'errores':errores}

           return render(request, 'paginas/personas_list.html', context)

    except:
        print("Error, rut no existe")
        errores.append("Error rut no encontrado.")
        context = {'personas': personas,  'mensajes': mensajes, 'errores':errores}
        return render(request, 'paginas/personas_list.html', context)
    
    
    


def personas_edit(request, pk):
    mensajes=[]
    errores=[]   
    
    context={}
    #productos = Producto.objects.all()
    #try:
    persona=Personas.objects.get(idPersona=pk)

    context={}
    if persona:
        print("Edit encontró a persona...")
        mensajes.append("Bien, datos actualizados...")

        context = {'persona': persona,  'mensajes': mensajes, 'errores':errores}

        return render(request, 'paginas/personas_edit.html', context)
    
    return render(request, 'paginas/personas_list.html', context)

##################      CARRITO     ######################### 

def agregar_producto(request, producto_id):

    carrito = Carrito(request)

    producto = Producto.objects.get(idProducto=producto_id)

    carrito.agregar(producto=producto)

    return redirect("carro")

def agregar_producto2(request, producto_id):

    carrito = Carrito(request)

    producto = Producto.objects.get(idProducto=producto_id)

    carrito.agregar_flores(producto=producto)

    return redirect("flores")

def eliminar_producto(request, producto_id):

    carrito = Carrito(request)

    producto = Producto.objects.get(idProducto=producto_id)

    carrito.eliminar(producto=producto)

    return redirect("carro")

def restar_producto(request, producto_id):

    carrito = Carrito(request)

    producto = Producto.objects.get(idProducto=producto_id)

    carrito.restar_carrito(producto=producto)

    return redirect("carro")


def limpiar_carro(request):

    carrito = Carrito(request)

    carrito.limpiar_carrito()

    return redirect("carro")

################     PEDIDOS    #######################

@login_required(login_url="loguear")
def procesar_pedido(request):
    venta=Venta.objects.create(user=request.user)
    carro=Carrito(request)
    detalle_venta=list()
    for key ,value in carro.carrito.items():
        producto=Producto.objects.get(idProducto=key)
        nuevaCantidad=producto.stock-value["cantidad"]
        Producto.objects.filter(idProducto=key).update(stock=nuevaCantidad)
        detalle_venta.append(DetalleVenta(

            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            venta=venta,
            
            
        ))
    
    DetalleVenta.objects.bulk_create(detalle_venta)

    messages.success(request,"La compra se ha realizado correctamente")

    return redirect("index")