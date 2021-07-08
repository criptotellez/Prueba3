from rest_framework import fields, serializers
from app.models import Denuncia

class DenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = ['idDenuncia', 'descripcionDenuncia', 'fechaDenuncia', 'categoria']