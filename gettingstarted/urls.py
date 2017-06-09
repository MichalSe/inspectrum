from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

import gettingstarted.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', gettingstarted.views.home, name='home'),
 #   url(r'^db', gettingstarted.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', gettingstarted.views.signup, name='signup'),
    url(r'^verified/$', gettingstarted.views.verified, name='verified'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^loginsuccess/$', gettingstarted.views.login_success, name='loginsuccess'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^inspectrum/$', gettingstarted.views.inspectrum, name="inspectrum"),
    url(r'^states/url/(?P<url>.+)/$', gettingstarted.views.StatesPerUserView.as_view(), name='user-states'),
]

urlpatterns += staticfiles_urlpatterns()