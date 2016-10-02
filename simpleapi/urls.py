from django.conf.urls import url, include
from .views import PostListView, PostDetailView


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^blog/$', PostListView.as_view(), name='post-list'),
    url(r'^blog/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-details'),
]
