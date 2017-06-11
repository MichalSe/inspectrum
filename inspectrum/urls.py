from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

import inspectrum.views

# Examples:
# url(r'^$', 'inspectrum.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', inspectrum.views.home, name='home'),
 #   url(r'^db', inspectrum.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', inspectrum.views.signup, name='signup'),
    url(r'^verified/$', inspectrum.views.verified, name='verified'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^loginsuccess/$', inspectrum.views.login_success, name='loginsuccess'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^inspectrum/$', inspectrum.views.inspectrum, name="inspectrum"),
    url(r'^states/url/(?P<url>.+)/$', inspectrum.views.StatesPerUserView.as_view(), name='user-states'),
]

urlpatterns += staticfiles_urlpatterns()