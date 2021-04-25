from django.contrib import admin
from socialsite.models import Post,Comment
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Post,PostAdmin)




# @admin.register(Post)
# class CommentAdmin(admin.ModelAdmin):
# 	list_display=['comment_description','post']
# admin.site.register(Post)
# admin.site.register(Comment)

# class CommentInline(admin.TabularInline):
#     model = Comment

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
# 	list_display = ('comment_description', 'post')
#     inlines = [CommentInline]


# class CommentsInline(admin.TabularInline):
#     model = Comments

# class PostsAdmin(admin.ModelAdmin):
#     inlines = [
#         CommentsInline,
#     ]
# admin.site.register(Post,PostAdmin)