from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>', views.ArticalDetailView.as_view(), name='article_view'),
    path('article/create', views.ArticleCreateView.as_view(), name='article_create'),
    # path('author/create', views.create_author),
    # path('article/<int:pk>/update', views.update_article),
    path('article/<int:pk>/update', views.ArticleUpdateView.as_view(), name='article_update'),
    # path('article/<int:pk>/update/delete', views.ArticleUpdateView.as_view(), name='article_delete'),
    path('article/<int:pk>/delete', views.delete_article, name='article_delete'),
    path('home/', views.home, name='home'),
    path('about', views.about, name='about'),
]
