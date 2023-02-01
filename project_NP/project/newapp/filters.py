from django_filters import FilterSet, CharFilter, DateTimeFilter, ModelChoiceFilter, ChoiceFilter
from .models import Post, Category
from django.forms import DateTimeInput
from django import forms

class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        )
    )

    post_category = ModelChoiceFilter(
        field_name = 'postCategory',
        queryset = Category.objects.all(),
        label = 'Категория публикации'

    )
    post_title = CharFilter(
        field_name = 'title',
        lookup_expr = 'icontains',
        label = 'Название публикации'
    )
    post_categoryType = ChoiceFilter(
        field_name='categoryType',
        label='ТИП',
        choices=Post.CATEGORY_CHOICES
    )
    class Meta:
        model = Post
        fields = {

        }