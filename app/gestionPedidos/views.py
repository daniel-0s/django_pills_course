from django.shortcuts import render
from django.http import HttpResponse

from gestionPedidos.models import Articulos

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def buscar_productos(request):
    return render(request,"busqueda_productos.html")

def buscar(request):

    if request.GET["producto_nombre"]: 
        #mensaje = "Producto buscado {0}".format(request.GET["producto_nombre"])
        product_name = request.GET["producto_nombre"]
        articulos = Articulos.objects.filter(nombre__icontains=product_name)
        return render(request ,"resultado_busqueda.html",{"articulos":articulos,"query":product_name})
    else:
        mensaje = "Introducir  producto"
    
        return HttpResponse(mensaje)

def contacto(request):

    if request.method == "POST":
        subject = request.POST["asunto"]
        mensaje = request.POST["mensaje"] + " "+ request.POST["email"]

        email_from =  settings.EMAIL_HOST_USER

        recipient_list = ["email_de_destino"]

        send_mail(subject,mensaje,email_from,recipient_list)

        return render(request,"gracias.html")

    return render(request,"contacto.html")