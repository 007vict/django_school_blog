from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from news.models import News, Category, Tag

class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text_min', 'text')

admin.site.register(News,NewsAdmin)
admin.site.register(Category)
admin.site.register(Tag)

