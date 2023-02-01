from django.urls import path
from .views import PostList, ShowPost, PostCreate, SearchList, PostUpdate, PostDelete

urlpatterns = [

   path('', PostList.as_view(), name='post_list'),
   path('search/', SearchList.as_view()),
   path('<int:pk>/', ShowPost.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view()),
   path('<int:pk>/edit/', PostUpdate.as_view()),
   path('<int:pk>/delete/', PostDelete.as_view())

]