from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True,allow_unicode=True)
    def get_url(self):
        return f'/blog/category/{self.slug}/'
    def __str__(self):
        return f'-이름:{self.name} -슬러그: {self.slug}'

#게시글클래스
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True,
                                        null=True)
    updated_date = models.DateTimeField(auto_now=True,
                                        null=True)
    uploaded_img = models.ImageField(upload_to='media/',
                                     blank=True,null=True)
    uploaded_file = models.FileField(upload_to='file/',
                                     blank=True,null=True)

    def __str__(self):
        return f'게시글 제목:{self.title} -작성자:{self.author}-게시글 내용:{self.content}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

#댓글클래스
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True,
                                        null=True)
    updated_date = models.DateTimeField(auto_now=True,
                                        null=True)
    def __str__(self):
        return (f'{self.author.username} -- {self.content}')



