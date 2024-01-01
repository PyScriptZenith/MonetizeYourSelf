from django import forms
from monetizeyourself.models import Post


class StyleMixin:
    """
    Класс для единой стилистики форм
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class PostForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Post

        fields = ("header", "text", "published_date", "is_free", "image")
        widgets = {"is_free": forms.Select(choices=((True, "Да"), (False, "Нет")))}

    published_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Дата публикации",
        required=False,
    )
