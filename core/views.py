from django.shortcuts import render
from .models import Question

def faq(request):
    questions = Question.objects.all()
    questions = questions[::-1]
    return render(request, 'core/faq.html', {'questions': questions,})

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def publications(request):
    return render(request, 'core/publications.html')

