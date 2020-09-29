from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all" : ("css/main.css",)
        }
        js = ("js/blog.js",)

admin.site.register(Question, QuestionAdmin)