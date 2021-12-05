from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'restaurant_name',
            'eval',
            'date_of_post',
            'content',
            'poster_url',
        ]
        labels = {
            'restaurant_name': 'Nome do Restaurante',
            'eval': 'Avaliação Geral do Restaurante (de 0 a 5)',
            'date_of_post': 'Data da ida no Restaurante',
            'content': 'Review de sua experiência',
            'poster_url': 'URL da foto do Restaurante',
        }