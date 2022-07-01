


from email.mime import image


class Carrito:
    def __init__(self,request): 
        self.request = request
        self.session = request.session
        carrito= self.session.get("carrito")
        if not carrito:
            carrito=self.session["carrito"]={}
        
        self.carrito=carrito

    def agregar_flores(self, producto):
        if(str(producto.idProducto) not in self.carrito.keys()):
            self.carrito[producto.idProducto]={
                "producto_id": producto.idProducto,
                "nombre":producto.nombreProducto,
                "precio": str(producto.precio),
                "cantidad": 1,
                "stock": producto.stock,
                "imagen": producto.foto.url
            }
        else:
            for key, value in self.carrito.items():
                if key==str(producto.idProducto):
                    value["cantidad"]=value["cantidad"]+1
                    break
        self.guardar_carrito()
    
    def agregar(self, producto):
        if(str(producto.idProducto) not in self.carrito.keys()):
            self.carrito[producto.idProducto]={
                "producto_id": producto.idProducto,
                "nombre":producto.nombreProducto,
                "precio": str(producto.precio),
                "stock":producto.stock,
                "cantidad": 1,
                "imagen": producto.foto.url
            }
        else:
            for key, value in self.carrito.items():
                if key==str(producto.idProducto):
                    value["cantidad"]=value["cantidad"]+1
                    
                    

                    
                    
                    break
                    
        self.guardar_carrito()
    
    

    def guardar_carrito(self):
        self.session["carrito"]=self.carrito
        self.session.modified=True

    def eliminar(self,producto):
        producto.idProducto=str(producto.idProducto)
        if producto.idProducto in self.carrito:
            del self.carrito[producto.idProducto] 
            self.guardar_carrito()

    def restar_carrito(self, producto):
        for key, value in self.carrito.items():
                if key==str(producto.idProducto):
                    value["cantidad"]=value["cantidad"]-1

                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break

        self.guardar_carrito()
    
    
    
    def limpiar_carrito(self):
        self.session["carrito"]={}
        self.session.modified=True