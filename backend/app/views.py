from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ShortenedURL
import json

@csrf_exempt
def shorten_url(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            original_url = data.get('url')
            
            if not original_url:
                return JsonResponse({'error': 'URL is required'}, status=400)
            
            shortened_url = ShortenedURL.objects.create(original_url=original_url)
            
            return JsonResponse({
                'original_url': shortened_url.original_url,
                'short_code': shortened_url.short_code,
                'short_url': f"{request.scheme}://{request.get_host()}/{shortened_url.short_code}"
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def redirect_to_original(request, short_code):
    shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
    shortened_url.clicks += 1
    shortened_url.save()
    return redirect(shortened_url.original_url)

def get_url_stats(request, short_code):
    shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
    return JsonResponse({
        'original_url': shortened_url.original_url,
        'short_code': shortened_url.short_code,
        'clicks': shortened_url.clicks,
        'created_at': shortened_url.created_at
    })


