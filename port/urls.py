from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# urlpatterns += patterns('portfolio.work.views',
# 	url(r'^$', 'project_list', name='project_list'),
# 	url(r'^project/(?P<projectslug>.*)/$', 'project_page', name='project_page'),
# )
# urlpatterns += patterns('portfolio.pages.views',
# 	url(r'^(?P<pageslug>.*)/$', 'page_detail', name='page'),
# )
# urlpatterns += patterns('portfolio.contact.views',
# 	url(r'^contact/$', 'contact', name='contact'),
# )

# #	Media URL
# if settings.DEBUG:
# 	urlpatterns += patterns('',
# 		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
# 	)

# urlpatterns += staticfiles_urlpatterns()