from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NegocioForm



def CrearNegocio(request):
    if hasattr(request.user, 'negocio'):                                            # hasattr: funcion que verifica si un objeto tiene un atributo especifico hasattr(objeto, 'atributo')
        messages.warning(request, "Ya tenes un negocio creado")
        return redirect("home")

    if request.method == 'POST':

        form = NegocioForm(request.POST)

        if form.is_valid():

            negocio = form.save(commit=False)
            negocio.administrador = request.user
            negocio.save()

            messages.success(request, "Negocio creado correctamente. Bienvenido/a!")
            return redirect("home")
        
        else:

            print(form.errors)  # esto ayuda a debug
            messages.error(request, "Error en el formulario. Revisá los datos")

    else:
        
        form = NegocioForm()

    return render(request, 'negocio/crear_negocio.html', {"form": form})
