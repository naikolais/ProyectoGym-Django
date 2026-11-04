from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import PlanEntrenamiento
from .forms import PlanEntrenamientoCrearForm, PlanEntrenamientoEditarForm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .serializers import PlanEntrenamientoSerializer


# --- API REST VIEWS ---
class PlanEntrenamientoViewSet(viewsets.ModelViewSet):
    queryset = PlanEntrenamiento.objects.all().order_by('-fecha_creacion')
    serializer_class = PlanEntrenamientoSerializer
    # Requerimiento de Token y autenticación para la API
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


# --- VISTAS WEB DEL CRUD Y PÚBLICAS ---
def inicio(request):
    total_planes = PlanEntrenamiento.objects.count()
    return render(request, 'planes/inicio.html', {'total_planes': total_planes})


def listar_planes(request):
    planes = PlanEntrenamiento.objects.all().order_by('-fecha_creacion')
    return render(request, 'planes/listar.html', {'planes': planes})


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def eliminar_plan(request, pk):
    plan = get_object_or_404(PlanEntrenamiento, pk=pk)
    if request.method == 'POST':
        plan.delete()
        messages.success(request, 'Plan eliminado correctamente.')
        return redirect('listar_planes')
    return render(request, 'planes/eliminar.html', {'plan': plan})


# --- VISTAS DE AUTENTICACIÓN WEB (LOGIN / LOGOUT) ---
def login_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        user = authenticate(request, username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            messages.success(request, "¡Sesión iniciada correctamente!")
            return redirect('listar_planes')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, 'planes/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect('inicio')

def vista_obtener_token(request):
    return render(request, 'planes/obtener_token.html')