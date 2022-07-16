from django.http import HttpResponse
from django.template import Context, Template

def template1(request):

    mihtml=open("C:/Users/Tin/Documents/ArVSC/CoderHouse/Proyecto1/Proyecto1/Plantillas/Template.html")
    plantilla=Template(mihtml.read())
    mihtml.close
    miContexto=Context()
    documento=plantilla.render(miContexto)
    return HttpResponse(documento)
    