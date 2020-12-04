from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import ARTICULOS
from django.core.mail import send_mail
from django.conf import settings
from GestionPedidos.forms import FormulariodeContacto

# Create your views here.

#vista para BuscarProductos

def BusquedaProductos(request):

    return render(request,"BusquedaProductos.html")

#vista para el resultado de la busqueda

def Buscar(request):

    if request.GET["Busproductos"]: 

        #mensaje="Articulo Buscado: %r" %request.GET["Busproductos"]
        producto=request.GET["Busproductos"]

        #para limitar la cantidad de caracteres en la busqueda

        if len(producto)>20:

            mensaje="Texto demaciado largo"

        else:


            articulos=ARTICULOS.objects.filter(nombrearticulo__icontains=producto)

            return render(request,"ResultadosdelaBusqueda.html",{"articulos":articulos,"query":producto})

    else:

        mensaje="Tienes que Indicar un Producto"

    return HttpResponse(mensaje)


# vista para el formulario de contacto para solicitud

def contacto(request):

    if request.method=="POST":

       # VariableAsunto=request.POST["asunto"]


      # VariableMensajeEmail=request.POST["mensaje"] + " " + request.POST["email"]

        #de donde viene el email

        #VariableEmail=settings.EMAIL_HOST_USER

        #VariableEmailDestino=["navago13@hotmail.com"]

        #send_mail(VariableAsunto,VariableMensajeEmail,VariableEmail,VariableEmailDestino)

        #return render(request,"GRACIAS.html")


    #return render(request,"Contacto.html")

        miformulario=FormulariodeContacto(request.POST)

        if miformulario.is_valid():

            informaciondeformulario=miformulario.cleaned_data

            #email se deja en '' blanco o se coloca el de settings

            send_mail(informaciondeformulario['asunto'],informaciondeformulario['mensaje'],informaciondeformulario.get('email',''),['navago13@hotmail.com'],)

            return render(request,"GRACIAS.html")
    else:
        
        miformulario=FormulariodeContacto()

    return render(request,"formulariodecontacto.html",{"form":miformulario})