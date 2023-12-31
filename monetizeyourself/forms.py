from django import forms

from monetizeyourself.models import Post


class StyleMixin:
    """
    Класс для единой стилистики форм
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class PostForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ('owner', 'header', 'text', 'published_date',
                                    'published_date', 'is_free', 'image')

    published_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                     label='Дата публикации', required=False)


