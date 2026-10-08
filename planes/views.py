from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import PlanEntrenamiento
from .forms import PlanEntrenamientoCrearForm, PlanEntrenamientoEditarForm

def inicio(request):
    total_planes = PlanEntrenamiento.objects.count()
    return render(request, 'planes/inicio.html', {'total_planes': total_planes})

def listar_planes(request):
    planes = PlanEntrenamiento.objects.all().order_by('-fecha_creacion')
    return render(request, 'planes/listar.html', {'planes': planes})

def crear_plan(request):
    if request.method == 'POST':
        form = PlanEntrenamientoCrearForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡El plan fue creado exitosamente!')
            return redirect('listar_planes')
    else:
        form = PlanEntrenamientoCrearForm()
    return render(request, 'planes/crear.html', {'form': form})

def editar_plan(request, pk):
    plan = get_object_or_404(PlanEntrenamiento, pk=pk)
    if request.method == 'POST':
        form = PlanEntrenamientoEditarForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, '¡El plan fue actualizado!')
            return redirect('listar_planes')
    else:
        form = PlanEntrenamientoEditarForm(instance=plan)
    return render(request, 'planes/editar.html', {'form': form, 'plan': plan})

def eliminar_plan(request, pk):
    plan = get_object_or_404(PlanEntrenamiento, pk=pk)
    if request.method == 'POST':
        plan.delete()
        messages.success(request, 'Plan eliminado correctamente.')
        return redirect('listar_planes')
    return render(request, 'planes/eliminar.html', {'plan': plan})