from venv import create
from django.conf.urls import include, url
from django.contrib import admin
from groceryapp import views
from groceryapp.views import delete_view
urlpatterns = [
    # Examples:
    # url(r'^$', 'grocerypro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^admin/', include(admin.site.urls)),
    url('^check/', views.retrieve_view),
    url('^create/', views.create_view, name='create'),
    url('^Addlist/', views.create_view, name='create'),
    url(r'^delete/(?P<id>[0-9]+)$', views.delete_view, name='delete'),
    url(r'^update/(?P<id>[0-9]+)$', views.update_view, name='update'),
]
