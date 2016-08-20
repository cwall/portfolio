from pages.models import Pages
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
#from contact.forms import ContactForm

def page_detail(request, pageslug):
	page = get_object_or_404(Pages, slug=pageslug)
	form = ContactForm()
	return render_to_response('pages/pages.html', {'page':page, 'form':form}, context_instance=RequestContext(request))	
