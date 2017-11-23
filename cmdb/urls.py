from django.conf.urls import patterns, include, url
from django.contrib import admin
from app04 import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cmdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app04/', include('app04.urls')),
)
