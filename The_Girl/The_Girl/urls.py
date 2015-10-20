from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

# UNDERNEATH your urlpatterns definition, add the following two lines:



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'girlgod.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('follow_the_girl.urls')),
    url(r'^save/', include('follow_the_girl.urls')),
    url(r'^$', include('follow_the_girl.urls')),
)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), 
    )