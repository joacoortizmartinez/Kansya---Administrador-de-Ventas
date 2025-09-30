from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import RegistroAdminForm, RegistroEmpleadoForm
from .models import Perfil
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth import login



# Create your views here.

def RegistrarAdmin(request):
    if(request.method == 'POST'):
        # Proceso de form para registrar un admin
        form = RegistroAdminForm(request.POST)

        if form.is_valid():
            try:
                user = form.save(commit=False)                                      #genero usuario sin guardar en la bd
                user.set_password(form.cleaned_data["password"])                    #hasheo de la contraseña
                user.save()                                                         #guardo el usuario en la bd

                Perfil.objects.create(usuario=user, rol="ADMINISTRADOR")

                 # Loguear  al nuevo admin
                login(request, user)

                messages.success(request, "Administrador creado correctamente")
                return redirect("iniciar_negocio")
            except Exception as e:
                messages.error(request, f"Error: {e}")
    else:
        form = RegistroAdminForm()

    return render(request, "usuarios/registro_admin.html", {"form": form})


@login_required
def RegistrarEmpleado(request):
    if request.user.perfil.rol != "ADMINISTRADOR":
        raise PermissionDenied("No tienes permiso para crear empleados")
    
    if(request.method == 'POST'):
        form = RegistroEmpleadoForm(request.POST)

        if form.is_valid():
            try:
                empleado = form.save(commit=False)                                      
                empleado.set_password(form.cleaned_data["password"])                    
                empleado.save()                                                        

                Perfil.objects.create(usuario=empleado, rol="EMPLEADO")

                messages.success(request, "Empleado creado correctamente")
                return redirect("home")
            
            except Exception as e:
                messages.error(request, f"Error: {e}")
    else:
        form = RegistroAdminForm()

    return render(request, "usuarios/registro_empleado.html")