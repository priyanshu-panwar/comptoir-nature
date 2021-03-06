from django.shortcuts import render
from .models import Question
from facebook_scraper import get_posts
from .models import Post, Category, Contact, Utility, Text
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from comptoir.settings import EMAIL_HOST_USER, ADMIN_MAIL, SCRAPE_DATE
from datetime import date
from django.conf import settings

import requests
from bs4 import BeautifulSoup
from json import loads

def extract_insta():
	URL = 'https://www.instagram.com/deco_comptoirnature/'
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')
	scripts = soup.find_all('script')
	data_script = scripts[4]

	content = data_script.contents[0]
	data_object = content[content.find('{"config"'):-1]
	data_json = data_object.json()
	# data_json = loads(data_object)
	need = data_json['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
	for i in range(22):
		print(f"Post {i}\n")
		try:
			if (len(need) > 0 and len(need[i]) > 0):
				hell = need[i]['node']
			else:
				continue
			print("Image = " , hell['display_url'])
			if (len(hell['edge_media_to_caption']['edges'])):
				print("Text = " , hell['edge_media_to_caption']['edges'][0]['node']['text'])
			else:
				print("No caption")
			print("\n\n")
			image = hell['display_url']
			text = "comptoirNature"
			if (len(hell['edge_media_to_caption']['edges'])):
				text = hell['edge_media_to_caption']['edges'][0]['node']['text']
			fun = False
			for x in Post.objects.all():
				if (x.image == image):
					fun = True
					break
			if fun:
				continue
			p = Post()
			p.image = image
			p.text = text
			string = text
			res = ""
			start = string.find("***") + len("***")
			end = string.rfind("***")
			substring = string[start:end]
			print(substring)
			p.title = substring
			p.save()
		except:
			continue		

def extract_images(idx):
	print("extracting.........\n.......\n......\n")
	for post in get_posts('comptoirnaturejarry', pages=idx):
		print(post['text'])
		print(post['image'])
		print(post['post_url'])
		if post['image'] and post['text'] and len(post['image']) > 25:
			p = Post()
			p.image = post['image'][0]
			p.text = post['text']
			string = post['text']
			res = ""
			start = string.find("***") + len("***")
			end = string.rfind("***")
			substring = string[start:end]
			print(substring)
			p.title = substring
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
    posts = Post.objects.all()
    posts = posts[::-1]
    lposts = posts[:3]
    return render(request, 'core/faq.html', {'questions': questions, 'lposts':lposts,})

def contact(request):
    return render(request, 'core/contact.html')

def publications(request):
	today = date.today()
	year = int(today.strftime("%Y"))
	month = int(today.strftime("%m"))
	day = int(today.strftime("%d"))

	key = year*10000 + month*100 + day
	print(key)
	print(settings.SCRAPE_DATE)

	if key != settings.SCRAPE_DATE :
		extract_insta()
		settings.SCRAPE_DATE = key
	print(settings.SCRAPE_DATE)

	posts = Post.objects.all()
	posts = posts[::-1]
	lposts = posts[:3]

	page = request.GET.get('page', 1)
	paginator = Paginator(posts, 12)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	# posts = posts[::-1]
	return render(request, 'core/publications.html', {'posts':posts, 'lposts':lposts,})



def index(request):
	text = Text.objects.all()
	text = text[0]
	posts = Post.objects.all()
	posts = posts[::-1]
	lposts = posts[:3]
	categories = Category.objects.all()
	categories = categories[::-1]
	context = {
		'categories' : categories,
		'lposts' : lposts,
		'text' : text,
	}
	return render(request, 'core/index.html', context)
    # return render(request, 'core/index.html', context)

def is_valid_queryparam(param):
	return param != '' and param is not None


def contact(request):
	text = Text.objects.all()
	text = text[0]
	posts = Post.objects.all()
	posts = posts[::-1]
	lposts = posts[:3]
	util = Utility.objects.all()
	util = util[::-1]
	util = util[-1]

	name = request.GET.get('contact-name')
	email = request.GET.get('contact-email')
	phone = request.GET.get('contact-phone')
	subject = request.GET.get('contact-subject')
	message = request.GET.get('contact-message')
	print(name)
	print(email)
	print(phone)
	print(subject)
	print(message)
	
	if is_valid_queryparam(name) and is_valid_queryparam(email) and is_valid_queryparam(message):
		c = Contact(name=name, email=email, telephone=phone, subject=subject, message=message)
		c.save()
		send_mail(
			'Thank you for contacting - comptoirnature.net',
			'Thank you for Contacting. Will get back to you.',
			EMAIL_HOST_USER,
			[email, ],
			fail_silently=True,
		)
		send_mail(
			f'NEW CONTACT - {email}',
			f'{message}',
			EMAIL_HOST_USER,
			[ADMIN_MAIL, ],
			fail_silently=True,
		)
		return render(request, 'core/thankyou.html')

	return render(request, 'core/contact.html', {'util' : util, 'lposts' : lposts, 'text' : text, })