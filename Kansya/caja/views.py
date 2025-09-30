from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from caja.models import Caja
from informe.models import Informe
from caja.forms import CajaForm, CerrarCajaForm
from django.contrib import messages


# Create your views here.
@login_required
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


@login_required
def CerrarCaja(request):
    if not Caja.objects.filter(estado="ABIERTA").exists():
        messages.warning(request, "No tenes ninguna caja abierta para cerrar.")
        return redirect("abrir_caja")
    
    if (request.method == 'POST'):
        form = CerrarCajaForm(request.POST)
        if form.is_valid():

            caja = Caja.objects.get(estado="Abierta")
            caja.monto_final = form.cleaned_data['monto_final']
            caja.usuario_cierre = form.cleaned_data['usuario_cierre']
            caja.estado = "Cerrada"
            caja.save()

            informe = Informe.objects.create(
                caja=caja,
                monto_inicial=caja.monto_inicial,
                monto_final=caja.monto_final,
                usuario_cierre=caja.usuario_cierre,

            )
            messages.success(request, "Caja cerrada exitosamente.")
            return redirect("informe")
    else:
        form = CerrarCajaForm()

    return render(request, 'caja/cerrar_caja.html', {'form': form})
