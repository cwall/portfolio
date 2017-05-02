from .models import Pages
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
#from contact.forms import ContactForm

def page_detail(request, pageslug):
	page = get_object_or_404(Pages, slug=pageslug)
	form = ContactForm()
	return render('pages/pages.html', {'page':page, 'form':form}, context_instance=RequestContext(request))	
