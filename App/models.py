from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Maqola nomi')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField()
    like = models.ForeignKey('Typer',on_delete=models.CASCADE, verbose_name='Yoqtirganlar soni',null=True,blank=True)



    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(blank=True, null=True, verbose_name='Post matni')
    blog = models.ForeignKey(Blog,verbose_name='Blog nomi ',on_delete=models.SET_NULL,null=True)
    typer = models.ForeignKey('Typer', verbose_name='Izoh muallifi', on_delete=models.SET_NULL,null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.typer.name




class Typer(models.Model):
    name = models.CharField(max_length=150,verbose_name='Comment muallifi')
    born_date = models.DateField()


    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Maqola muallifi')
    born_date = models.DateField()

    def __str__(self):
       return self.name


class Post(models.Model):
    nomi = models.CharField(max_length=150, verbose_name='Maqola mavzusi')
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True, verbose_name='Maqola matni')
    author = models.ForeignKey(Author,verbose_name='Post muallifi', on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.nomi