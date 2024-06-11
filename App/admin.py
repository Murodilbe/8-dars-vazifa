from django.contrib import admin
from .models import Blog,Author,Post,Typer,Comment
# Register your models here.
admin.site.register(Blog)
admin.site.register(Typer)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Post)