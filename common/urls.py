from django.conf.urls import url
from common import views
 
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    # url(r'^links/$' , views.LinksPageView.as_view()),
]