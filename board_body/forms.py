from django.forms import ModelForm

from board_body.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'