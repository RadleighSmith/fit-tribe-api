from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer

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