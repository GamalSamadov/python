from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from myapp.models import Author, Article
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
from myapp.forms import ArticleForm


# from django.core.exceptions import ObjectDoesNotExist
# from myapp.forms import ArticleForm, AuthorForm
# def hello_world(request):
#     # Can Fetch data from database.
#     return render(request, 'hello.html', {
#         'name': 'Gamal Samadov',
#         'categories': [
#             'Category 1',
#             'Category 2',
#             'Category 3',
#             'Category 4',
#             'Category 5',
#         ]
#     })


# def show_article(request, id, slug):
#     return render(request, 'article/show_article.html', {
#         'title': 'Article ' + str(id),
#         'content': "Article content " + str(slug)
#     })


# def articles(request):
#     ## order_by
#     ## first
#     ## last
#     ## latest - last sorted item
#     # models = Article.objects.order_by('-id', 'title')
#     # models = Article.objects.order_by('title')
#     ## pk__gt ==> greater then
#     ## pk__gte ==> greater then ot equal
#     ## pk__lt ==> less then
#     ## pk__lte ==> less then or equal
#     ## pk__range ==> in range of (n1, n2) this two numbers
#
#     # models = Article.objects.filter(pk__range=(0, 20))
#
#     ## title__contains ==> search by words LIKE %search word%
#     ## title_icontains ==> search by words capital words not means anything LIKE %search word%
#     ## title__srartswith ==> search by given number on the begining of title LIKE search word%
#     ## title__endswith ==> search by given number on the end of title LIKE %search word
#
#     # models = Article.objects.filter(title__icontains='1')
#
#     # models = Article.objects.select_related('author').all() # OneToOne, OneToMany
#     models = Article.objects.prefetch_related('tag').select_related('author').all()  # ManyToMany
#
#     return render(request, 'article/list.html', {
#         'articles': models
#     })


# def show_article(request, id):
#     # try:
#     #     model = Article.objects.get(pk=id) # pk ==> primery key
#     # except ObjectDoesNotExist:
#     #     model = None
#
#     model = Article.objects.filter(pk=id).first()  # pk ==> primery key
#     return render(request, 'article/list.html', {
#         'article': model
#     })


# def create_article(request):
# article = Article()
# article.title = 'Article name'
# article.content = 'Article Content'
# article.author = Author(1)
# article.save()
#
# return render(request, 'article/show.html', {
#     'article': article
# })


# def create_article(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             content = form.cleaned_data['content']
#             author = form.cleaned_data['author']
#             tags = form.cleaned_data['tags']
#             article = Article.objects.create(title=title, content=content, author=author)
#             article.tag.set(tags)
#             return redirect('/myapp/')
#     else:
#         form = ArticleForm()
#     return render(request, 'article/create.html', {
#         'form': form
#     })
#
## Create Article using FormView
# class ArticleCreateView(FormView):
#     form_class = ArticleForm
#     template_name = 'article/create.html'
#
#     # success_url = '/myapp/' ## Cannot use name of url
#
#     def get_success_url(self):
#         return reverse('article_list')
#
#     def form_valid(self, form):
#         article = Article.objects.create(
#             title=form.cleaned_data['title'],
#             content=form.cleaned_data['content'],
#             author=form.cleaned_data['author']
#         )
#         article.tag.set(form.cleaned_data['tags'])
#         return super().form_valid(form)


# def update_article(request, pk):
#     Article.objects.filter(pk=pk).update(title='New title 1')
#     article = Article.objects.get(pk=pk)  # pk ==> primery key
#     # article.title = 'New title'
#     # article.save()
#
#     return render(request, 'article/show.html', {
#         'article': article
#     })
#
# def create_author(request):
#     if request.method == 'POST':
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             Author.objects.create(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 birthDate=form.cleaned_data['birthDate'],
#                 bio=form.cleaned_data['bio']
#             )
#             return redirect('/myapp/')
#     else:
#         form = AuthorForm()
#     return render(request, 'author/create.html', {
#         'form': form
#     })


def delete_article(request, pk):
    article = Article.objects.filter(pk=pk)  # pk ==> primery key
    article.delete()

    # # delete articles thet's id bigger then 1
    # Article.objects.filter(pk__gt=1).delete()

    # # Delelte all articles from db
    # Article.objects.all().delete()
    return render(request, 'article/delete.html')


class ArticleListView(ListView):
    model = Article
    template_name = 'article/list.html'
    # context_object_name = 'articles'
    queryset = Article.objects.prefetch_related('tag').select_related('author')


class ArticalDetailView(DetailView):
    model = Article
    template_name = 'article/show.html'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article/create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article/update.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_list')


def home(request):
    # author = Author()
    # author.name = 'Paka'
    # author.email = 'Paka@example.com'
    # author.save()

    # Author.objects.create(
    #     name='Shakal',
    #     email='shakal@example.com'
    # )
    # num = 1
    # for ar in range(30):
    #     article = Article()
    #     article.title = 'Article' + str(num)
    #     article.content = 'Python article 4 content hare.'
    #     article.author = Author(3)
    #     article.save()
    #     num += 1

    return render(request, 'article/list.html')


def about(request):
    return render(request, 'about.html')
