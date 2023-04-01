from ..models import Tesouro
from django import forms


class SalvarTesouroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Tesouro
        fields = ['nome', 'quantidade', 'preco', 'img_tesouro']
        labels = {
            'img_tesouro': 'Imagem'
        }
