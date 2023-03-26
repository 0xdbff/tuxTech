from django.shortcuts import render

from django.http import JsonResponse
from .models import Media

def get_media(request):
    media_items = Media.objects.filter(image__isnull=False)
    media_list = [{'id': media.id, 'name': media.name, 'media_type': media.media_type, 'url': media.image.url} for media in media_items]
    return JsonResponse(media_list, safe=False)


# Create your views here.
