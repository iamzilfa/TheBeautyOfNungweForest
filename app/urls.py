from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    url(r'^$',views.index,name = 'index'),
    url(r'^new/upload$', views.upload_photo, name='upload'),
    url(r'^new/profile$', views.add_profile, name='edit'),
    url(r'^myprofile$',views.my_profile,name ='myprofile'),
    url(r'^onephoto/(\d+)$', views.one_photo, name='onephoto'),
    url(r'^search/$', views.search_photo, name='search'),
    url(r'^like/(\d+)/$',views.likes, name = 'like'),
    url(r'^comment/(\d+)/$', views.add_comment, name='comment'),
    url(r'^view_comment/(\d+)/$', views.comment, name='view'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)