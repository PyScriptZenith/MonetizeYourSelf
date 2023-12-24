from django import forms

from monetizeyourself.models import Post


# class PostForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()




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

    HEADER_CHOICES = (
        (1, 'Тема_1'),
        (2, 'Тема_2'),
        (3, 'Тема_3'),
    )
    header = forms.ChoiceField(choices=HEADER_CHOICES, label='Заголовок', required=False)
    published_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                     label='Дата публикации', required=False)


