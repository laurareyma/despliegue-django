from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def authors(request):
    authors = [
        'Laura Vanesa Reyes',
        'Ana María Cordero',
    ]
    return render(request, 'doc/authors.html', {'authors': authors})
