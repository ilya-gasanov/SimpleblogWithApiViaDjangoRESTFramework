from rest_framework import generics, permissions
from blog.models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-date')
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class PostDetailView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
