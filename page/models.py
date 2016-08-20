from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class Pages(models.Model):
	title = models.CharField(max_length=250)
	subtitle = models.CharField(max_length=350, blank=True)
	slug = models.SlugField(unique=True)
	date = models.DateField(auto_now=True)
	content = models.TextField()
	meta = models.CharField(max_length=900)
	publish = models.BooleanField()
	
	class Meta:
		ordering = ['title']
		verbose_name_plural = 'Pages'
		
	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse('page.views.pages', args=[str(self.slug)])

class Section(models.Model):
	title = models.CharField(max_length=250, blank=True)
	subtitle = models.CharField(max_length=350, blank=True)
	class_name = models.CharField(max_length=50, blank=True)
	id_name = models.CharField(max_length=50, blank=True, unique=True)
	page = models.ForeignKey(Pages)

	class Meta:
		ordering = ['title']
		verbose_name_plural = 'Section'