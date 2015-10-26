from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),

	url(r'^postlist/$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$',views.post_details,name='post_details'),
	url(r'^post/new/$',views.post_new,name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	
	url(r'^booklist/$', views.book_list, name='book_list'),
	url(r'^book/(?P<pk>[0-9]+)/$',views.book_details,name='book_details'),
	url(r'^book/new/$',views.book_new,name='book_new'),
	url(r'^book/(?P<pk>[0-9]+)/edit/$', views.book_edit, name='book_edit'),
	
	url(r'^fashionlist/$', views.fashion_list, name='fashion_list'),
	url(r'^fashion/(?P<pk>[0-9]+)/$',views.fashion_details,name='fashion_details'),
	url(r'^fashion/new/$',views.fashion_new,name='fashion_new'),
	url(r'^fashion/(?P<pk>[0-9]+)/edit/$', views.fashion_edit, name='fashion_edit'),
	
	url(r'^travellist/$', views.travel_list, name='travel_list'),
	url(r'^travel/(?P<pk>[0-9]+)/$',views.travel_details,name='travel_details'),
	url(r'^travel/new/$',views.travel_new,name='travel_new'),
	url(r'^travel/(?P<pk>[0-9]+)/edit/$', views.travel_edit, name='travel_edit'),
	
	url(r'^foodlist/$', views.food_list, name='food_list'),
	url(r'^food/(?P<pk>[0-9]+)/$',views.food_details,name='food_details'),
	url(r'^food/new/$',views.food_new,name='food_new'),
	url(r'^food/(?P<pk>[0-9]+)/edit/$', views.food_edit, name='food_edit'),
	
	url(r'^technologylist/$', views.technology_list, name='technology_list'),
	url(r'^technology/(?P<pk>[0-9]+)/$',views.technology_details,name='technology_details'),
	url(r'^technology/new/$',views.technology_new,name='technology_new'),
	url(r'^technology/(?P<pk>[0-9]+)/edit/$', views.technology_edit, name='technology_edit'),
	
	url(r'^aboutus/$', views.about_us , name = 'about_us'),
	url(r'^rewards/$', views.rewards , name = 'rewards'),
	url(r'^contactus/$', views.contact_us, name = 'contact_us'),
]