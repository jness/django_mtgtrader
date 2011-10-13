from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'trader.views.index'),
    url(r'^gatherer/(.*)$', 'trader.views.gatherer_lookup'),
)

urlpatterns += staticfiles_urlpatterns()
