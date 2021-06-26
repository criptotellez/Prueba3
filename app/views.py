from django.shortcuts import render, redirect
from .models import Denuncia
from .forms import DenunciaForm

def home (request):
    return render (request, 'app/home.html')
# Create your views here.
def iniciar (request):
    return render (request, 'app/iniciar.html')

def registrar (request):
    return render (request, 'app/registrar.html')


def homeDenuncia(request):
    denuncias = Denuncia.objects.all()

    datos = {
        'denuncias' : denuncias
    }
    return render (request, 'app/homeDenuncia.html', datos)

def form_denuncia(request):

    datos ={
        'form': DenunciaForm()
    }
    if request.method=='POST':
        formulario = DenunciaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'app/form_denuncia.html', datos)

def form_mod_denuncia(request, id):
    denuncia = Denuncia.objects.get(idDenuncia=id)

    datos = {
        'form' : DenunciaForm(instance=denuncia)
    }
    if request.method=='POST':
        formulario = DenunciaForm(data=request.POST, instance=denuncia)

        if formulario.is_valid:
            formulario.save()

            datos['mesaje'] = "Modificados correctamente"
            datos['form']= formulario

    return render(request, 'app/form_mod_denuncia.html', datos)

def form_del_denuncia(request, id):
    denuncia = Denuncia.objects.get(idDenuncia=id)
    denuncia.delete()

    return redirect(to="home")