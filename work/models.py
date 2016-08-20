from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

class Services(models.Model):
	title = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(unique=True)
	date = models.DateField(auto_now=True)
	content = models.TextField(blank=True)
	icon = models.ImageField(upload_to="./services/icons/", blank=True)
	
	class Meta:
		ordering = ['title']
		get_latest_by = 'date'
		verbose_name_plural = 'Services'
	
	def __unicode__(self):
		return self.title
		
class Tools(models.Model):
	title = models.CharField(max_length=250)
	slug = models.SlugField()
	icon = models.ImageField(upload_to="./services/tools/", blank=True)
	
	class Meta:
		ordering = ['title']
		verbose_name_plural = 'Tools'
		
	def __unicode__(self):
		return self.title
			
class Project(models.Model):
	logo = models.ImageField(upload_to="./client-logos/", blank=True)
	title = models.CharField(max_length=250, blank=True)
	slug = models.SlugField(unique=True)
	date = models.DateField(auto_now=True)
	services = models.ManyToManyField(Services, blank=True)
	tools = models.ManyToManyField(Tools, blank=True)
	content = models.TextField()
	url = models.URLField(blank=True)
	meta = models.CharField(max_length=900)
	weight = models.PositiveIntegerField(blank=True)
	personal = models.BooleanField()
	publish = models.BooleanField()
	
	class Meta:
		ordering = ['weight']
		get_latest_by = 'date'
	
	def __unicode__(self):
		return self.title	

	def get_absolute_url(self):
		return reverse('portfolio.work.views.project_page', args=[str(self.slug)])
		
class Pieces(models.Model):
	images = models.ImageField(upload_to="./samples/%Y/")
	title = models.CharField(max_length=200, blank=True)
	slug = models.SlugField(unique=True)
	date = models.DateField(auto_now=True)
	project = models.ForeignKey(Project)
	publish = models.BooleanField()
	
	class Meta:
		ordering = ['title']
		get_latest_by = 'date'
		verbose_name_plural = 'Pieces'
		
	def __unicode__(self):
		return self.title
