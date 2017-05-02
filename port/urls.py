from django.conf.urls import url
from django.contrib import admin
from work import views as work_views
from page import views as page_views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', work_views.project_list, name="project_list"),
	# url(r'^$', work_views.project_list, name='project_list'),
	url(r'^project/(?P<projectslug>.*)/$', work_views.project_page, name='project_page'),
	url(r'^(?P<pageslug>.*)/$', page_views.page_detail, name='page'),
]
# urlpatterns = [
# 	url(r'^contact/$', 'contact', name='contact'),
# ]

# if settings.DEBUG:
# 	urlpatterns += patterns('',
# 		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
# 	)

# urlpatterns += staticfiles_urlpatterns()