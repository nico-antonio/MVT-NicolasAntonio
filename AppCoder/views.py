from django.shortcuts import render
from django.http import HttpResponse
from  .models import Familiar
# Create your views here.

def familiar(request):
    madre=Familiar(nombre="Silvia", edad=59, fecha_de_nacimiento="1963-01-03", relacion="madre")
    padre=Familiar(nombre="Alfredo", edad=59, fecha_de_nacimiento="1963-06-22", relacion="padre")
    hermano=Familiar(nombre="Ramiro", edad=29, fecha_de_nacimiento="1993-08-31", relacion="hermano")
    madre.save()
    padre.save()
    hermano.save()
    texto=f"Mi nombre es {madre.nombre}, tengo {madre.edad} años, nací el {madre.fecha_de_nacimiento} y soy {madre.relacion} de Nico, Mi nombre es {padre.nombre}, tengo {padre.edad} años, nací el {padre.fecha_de_nacimiento} y soy {padre.relacion} de Nico, Mi nombre es {hermano.nombre}, tengo {hermano.edad} años, nací el {hermano.fecha_de_nacimiento} y soy {hermano.relacion} de Nico" 
    return HttpResponse(texto) 