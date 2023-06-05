from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthDate = models.DateTimeField(null=True)
    bio = models.TextField(null=True)

    def __str__(self):
        return '| Name: ' + self.name + ' | ' + 'Email: ' + self.email + ' |'


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    # article_set (Django adds this)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author = models.OneToOneField(Author, on_delete=models.PROTECT) # OneToOne
    author = models.ForeignKey(Author, on_delete=models.PROTECT)  # OneToMany
    tag = models.ManyToManyField(Tag)
