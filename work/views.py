from work.models import Pieces, Project, Tools, Services
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from contact.forms import ContactForm

def project_list(request):
	projects = Project.objects.all().order_by('weight').filter(publish=True)
	form = ContactForm()
	return render( request, 'index.html', {'projects': projects, 'form':form}, context_instance=RequestContext(request))

def project_page(request, projectslug):
	project = get_object_or_404(Project, slug=projectslug)
	form = ContactForm()
	return render( request, '/project-single.html', {'project': project, 'form':form}, context_instance=RequestContext(request))
	
def piece_link(request, pieceslug):
	piece = get_object_or_404(Pieces, slug=pieceslug)
	return HttpResponse()
