from django.conf.urls import url

from .views import show_blogx,get_blogx


urlpatterns = [
    url(r'^$', show_blogx),
    url(r'^(?P<todo_id>[0-9]+)', get_blogx)


]
