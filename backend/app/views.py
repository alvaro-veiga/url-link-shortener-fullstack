from django.shortcuts import redirect, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer

class ShortenedURLViewSet(viewsets.ModelViewSet):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

@api_view(['GET'])
@permission_classes([AllowAny])
def redirect_to_original(request, short_code):
    shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
    shortened_url.clicks += 1
    shortened_url.save()
    return redirect(shortened_url.original_url)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_url_stats(request, short_code):
    shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
    serializer = ShortenedURLSerializer(shortened_url, context={'request': request})
    return Response(serializer.data)


