from django.contrib import admin
from .models import Post,Category,Small_Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'author','publish','status')
    search_fields = ('title','body',)
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish',)

admin.site.register(Category)

admin.site.register(Small_Category)