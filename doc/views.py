from django.shortcuts import render

# Create your views here.

def authors(request):
    authors = [
        'Laura Vanesa Reyes',
        'Ana María Cordero',
    ]
    return render(request, 'doc/authors.html', {'authors': authors})
