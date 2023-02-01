from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Category, Author


class PostForm(forms.ModelForm):
    author = forms.ModelChoiceField(label='Автор', queryset=Author.objects.all(), empty_label=())
    title = forms.CharField(label='Заголовок')
    postCategory = forms.ModelMultipleChoiceField(
        label='Категория',
        queryset=Category.objects.all(),
    )
    categoryType = forms.ChoiceField(
        label='ТИП',
        choices=Post.CATEGORY_CHOICES
    )

    class Meta:
        model = Post
        fields = ['text', 'categoryType', 'author', 'title', 'postCategory' ]


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("title")
        description = cleaned_data.get("text")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return name