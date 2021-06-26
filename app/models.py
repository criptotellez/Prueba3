from django.db import models

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True , verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50 , verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria

class Denuncia(models.Model):
    idDenuncia = models.CharField(max_length=6 , primary_key=True, verbose_name='idDenuncia')
    descripcionDenuncia =  models.CharField(max_length=300, verbose_name='descripcionDenuncia')
    fechaDenuncia = models.CharField(max_length=20, null=True , blank=True , verbose_name='fechaDenuncia')
    categoria = models.ForeignKey(Categoria , on_delete= models.CASCADE)

    def __str__(self):
        return self.idDenuncia