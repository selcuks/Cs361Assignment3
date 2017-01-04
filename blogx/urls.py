from django.conf.urls import url




from .views import *

urlpatterns = [
    url(r'^$', show_blogx),
    url(r'^(?P<blogx_id>[0-9]+)', get_blogx),
    url(r'^all/$', show_all_blogx),
    url(r'^all/user/(?P<blogxId>[0-9]+)$', show_all_blogx_from_user),

    ]