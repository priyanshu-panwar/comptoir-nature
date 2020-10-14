from django.contrib import admin
from .models import Question, Post, Category, Contact, Utility

admin.site.register(Category)
# admin.site.register(Post)
admin.site.register(Contact)
# admin.site.register(Utility)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'date']
	list_filter = ['date', ]
	search_fields = ('title',)


class QuestionAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all" : ("css/main.css",)
        }
        js = ("js/blog.js",)

admin.site.register(Question, QuestionAdmin)



class UtilityAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all" : ("css/main.css",)
        }
        js = ("js/util.js",)

admin.site.register(Utility, UtilityAdmin)