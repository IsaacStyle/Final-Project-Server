from django.contrib import admin
from .models import Post,User,Comments,Subs
# Register your models here.
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Subs)
admin.site.register(Comments)