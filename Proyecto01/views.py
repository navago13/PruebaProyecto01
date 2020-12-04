from django.http import HttpResponse
import datetime
from datetime import datetime
from django.template import Template,Context
from django.template.loader import  get_template
from django.shortcuts import render


class Persona(object):  # una Clase 

    def __init__(self, nombre, apellido):  # metodo

        self.nombre=nombre
        self.apellido=apellido 

def saludo(request): # esta es la primera vista

    p1 = Persona(" Jose Aristides","GONZALEZ NAVARRO")

    TemasdelCurso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]  # una Lista   
    ahora=datetime.now()

   # documentoExterno=open("C:/Users/josegonzalez/Desktop/ProyectoDjango/Proyecto01/Proyecto01/Plantillas/miPrimeraPlantilla.html")

    #plt=Template(documentoExterno.read())

    #documentoExterno.close()

    #documentoExterno=get_template('miprimeraPlantilla.html')

    #ctx=Context({"nombrepersona": p1.nombre , "apellidopersona": p1.apellido , "horaActual":ahora,"Temas":TemasdelCurso})

    #documento=plt.render(ctx)
    # se le pasa un diccionario en vez de un contexto
    #documento=documentoExterno.render({"nombrepersona": p1.nombre , "apellidopersona": p1.apellido , "horaActual":ahora,"Temas":TemasdelCurso})

    #return HttpResponse(documento)
    return render(request,"miPrimeraPlantilla.html",{"nombrepersona": p1.nombre , "apellidopersona": p1.apellido , "horaActual":ahora,"Temas":TemasdelCurso})

def Herencia(request):

    ahora=datetime.now()

    return render(request,"CursoC.html",{"dameFecha":ahora})
    
def despedida(request):# segunada vista

    return HttpResponse("Esta es la Despedida de la Primera Pagina")    

def  damefecha(request):

    fecha_actual=datetime.datetime.now()

    documento= """<html>
    <boody>
    <h1>
    FECHA Y HORA ACTUALES %s
    </h1>
    </boody>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def EDAD(request,edad02,abno):

     edad01= (abno-2019)+edad02

     documento= """<html>
     <boody>
     <h2>
     EN ESE AÑO %s TENDRAS ESTA EDAD %s
     </h2>
     </boody>
     </html>""" % (abno,edad01)
     return HttpResponse(documento)