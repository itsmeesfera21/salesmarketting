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
    url(r'^post/(?P<slug>.*)/edit/$', views.post_edit, name='post_edit'),
    url(r'^category/(?P<pk>\d+)$', views.post_category, name='post_category'),
    url(r'drafts/$',views.post_draft_list,name="post_draft_list"),
    url(r'^drafts/publish/(?P<slug>.*)/',views.post_publish,name='post_publish'),
    url(r'post/new/$',views.post_new,name="post_new"),
    url(r'post/delete/(?P<slug>.*)/',views.post_delete,name="post_delete"),
    url(r'^post/(?P<slug>.*)/',views.post_detail,name='post_detail')
]