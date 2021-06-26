from django.http.response import HttpResponseNotModified
from django.urls import path
from .views import home
from .views import iniciar
from .views import registrar
from .views import form_denuncia, homeDenuncia, form_mod_denuncia, form_del_denuncia


urlpatterns = [
    path('home.html', home, name = "home"),
    path('iniciar.html', iniciar, name= "iniciar"),
    path('registrar.html', registrar, name= "registrar"),
    path('home-denuncia.html', homeDenuncia, name="home"),
    path('form-denuncia', form_denuncia, name="form_denuncia"),
    path('form-mod-denuncia/<id>', form_mod_denuncia, name="form_mod_denuncia"),
    path('form-del-vehiculo/<id>', form_del_denuncia, name="form_del_denuncia"),

    ]