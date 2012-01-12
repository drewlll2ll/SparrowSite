from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('mainsite.views',
    # Examples:
    # url(r'^$', 'sparrow_lab.views.home', name='home'),
    # url(r'^sparrow_lab/', include('sparrow_lab.foo.urls')),

    # Example main page
    url(r'^$', 'index')
)