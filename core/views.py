from django.shortcuts import render
from .models import Question
from facebook_scraper import get_posts
from .models import Post

def extract_images(idx):
	for post in get_posts('comptoirnaturejarry', pages=idx):
		if post['text']:
			p = Post()
			p.image = post['image'][0]
			p.text = post['text']
			p.url = post['post_url']
			# p.date = post['date']
			p.save()
		else:
			return

def upload_all(request):
	extract_images(15)
	return render(request, 'core/publications.html')


def faq(request):
    questions = Question.objects.all()
    questions = questions[::-1]
    return render(request, 'core/faq.html', {'questions': questions,})

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def publications(request):
	posts = Post.objects.all()
	# posts = posts[::-1]
	return render(request, 'core/publications.html', {'posts':posts,})
