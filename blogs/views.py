from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer
from ft_api.permissions import IsOwnerOrReadOnly


class BlogList(APIView):
    serializer_class = BlogSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(
            blogs, many=True, context={'request' : request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BlogSerializer(
            data=request.data, context={'request' : request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
        
class BlogDetail(APIView):
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_object(self, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            self.check_object_permissions(self.request, blog)
            return blog
        except Blog.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        blog = self.get_object(pk)
        seralizer = BlogSerializer(
            blog, context={'request' : request}
        )
        return Response(seralizer.data)
    
    def put(self, request, pk):
        blog = self.get_object(pk)
        serialzier = BlogSerializer(
            blog, data=request.data, context={'request' : request}
        )
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data)
        return Response(
            serialzier.errors, status=status.HTTP_400_BAD_REQUEST
        )
        
    def delete(self, request, pk):
        blog = self.get_object(pk)
        blog.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        