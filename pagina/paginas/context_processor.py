def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        if 'carrito' in request.session:
            for key, value in request.session["carrito"].items():

                
                total=total+(float(value["precio"])*value["cantidad"])
    return {"importe_total_carro":total}