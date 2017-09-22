from django.contrib import admin
from TestModel.models import Test
from TestModel.models import Album
from TestModel.models import article

# Register your models here.
admin.site.register(Test)
admin.site.register(Album)
admin.site.register(article)