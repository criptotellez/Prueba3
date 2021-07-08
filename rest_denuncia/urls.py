from django.urls import path
from rest_denuncia.views import lista_denuncia, detalle_denuncia
from rest_denuncia.viewsLogin import login

urlpatterns = [
    path('lista_denuncia', lista_denuncia, name="lista_denuncia"),
    path('detalle_denuncia/<id>', detalle_denuncia, name= "detalle_denuncia"),
    path('login', login, name="login"),



]
