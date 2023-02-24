from django.http import request
from django.shortcuts import render

def index(request):
    remote_addr = request.META["REMOTE_ADDR"]
    context = {
        "remote_addr": remote_addr
    }
    return render(request, "index.html", context)
