from django.conf.urls import url
from . import views

# ^ for the beginning of the text
# $ for the end of the text
# \d for a digit
# + to indicate that the previous item should be repeated at least once
# () to capture part of the pattern

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^posts/$', views.post_all, name='post_all'),
    url(r'^post/(?P<slug>.*)/',views.post_detail,name='post_detail')
]