from django.shortcuts import render, redirect
from caja.models import Caja
from caja.forms import CajaForm
from django.contrib import messages


# Create your views here.

def AbrirCaja(request):
    if Caja.objects.filter(estado="ABIERTA").exists():
        messages.warning(request, "Ya tenes una caja abierta, cierra la caja actual para abrir una nueva.")
        return redirect("home")

    if request.method == 'POST':
        form = CajaForm(request.POST, negocio=request.user.negocio)
        if form.is_valid():
            caja = form.save(commit=False)
            caja.negocio = request.user.negocio
            caja.estado = "Abierta"
            caja.save()
            messages.success(request, "Caja abierta exitosamente.")
            return redirect("home")
    else:
        form = CajaForm(negocio=request.user.negocio)     
    return render(request, 'caja/abrir_caja.html', {'form': form})