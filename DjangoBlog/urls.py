from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^articles/', include('article.urls')),
    # Examples:
    # url(r'^$', 'DjangoBlog.views.home', name='home'),
    # url(r'^DjangoBlog/', include('DjangoBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User registration
    url(r'^accounts/login/$', 'DjangoBlog.views.login'),
    url(r'^accounts/auth/$', 'DjangoBlog.views.auth_view'),
    url(r'^accounts/logout/$', 'DjangoBlog.views.logout'),
    url(r'^accounts/loggedin$', 'DjangoBlog.views.loggedin'),
    url(r'^accounts/invalid/$', 'DjangoBlog.views.invalid_login'),
  	url(r'^accounts/register/$', 'DjangoBlog.views.register_user'),
  	url(r'^accounts/register_success/$', 'DjangoBlog.views.register_success'),  
  	  

)
