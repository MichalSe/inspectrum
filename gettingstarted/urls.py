from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

admin.autodiscover()

import gettingstarted.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', gettingstarted.views.home, name='home'),
    url(r'^db', gettingstarted.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', gettingstarted.views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^inspectrum/$', gettingstarted.views.inspectrum, name="inspectrum"),
]

