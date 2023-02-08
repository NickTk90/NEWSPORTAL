from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Post

from django.urls import reverse_lazy, reverse

from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView

from django.shortcuts import render

from .filters import PostFilter

from .forms import PostForm

class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-dateCreation'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'posts.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    paginate_by = 10


class SearchList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'search.html'
    context_object_name = 'posts'
    paginate_by = 5

        # Переопределяем функцию получения списка товаров
    def get_queryset(self):
            # Получаем обычный запрос
        queryset = super().get_queryset()
            # Используем наш класс фильтрации.
            # self.request.GET содержит объект QueryDict, который мы рассматривали
            # в этом юните ранее.
            # Сохраняем нашу фильтрацию в объекте класса,
            # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
            # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
            # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

    # def post_list(request):
    #     f=PostFilter(request.GET, queryset=Post.objects.all())
    #     return render(request, 'posts.html', {'filter': f})


class ShowPost(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'




# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'posts.html', context={'posts':posts})


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('newapp.add_post',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'create.html'
    success_url = reverse_lazy('post_list')

class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('newapp.change_post',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'edit.html'
    success_url = reverse_lazy('post_list')


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('newapp.delete_post',)
    raise_exception = True
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post_list')