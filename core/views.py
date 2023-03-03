from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, 'index.html')


def portfolio(request):
    # Get portfolio section data from database or other source
    portfolio_data = { 'title': 'My portfolio', 'projects': [ ... ] }

    # Render the base template with portfolio section content
    return render(request, 'index.html', { 'section': 'portfolio', 'data': portfolio_data })

def about(request):
    # Get about section data from database or other source
    about_data = { 'title': 'About me', 'content': '...' }

    # Render the base template with about section content
    return render(request, 'index.html', { 'section': 'about', 'data': about_data })

def contact(request):
    # Get contact section data from database or other source
    contact_data = { 'title': 'Contact me', 'email': '...', 'phone': '...', 'address': '...' }

    # Render the base template with contact section content
    return render(request, 'index.html', { 'section': 'contact', 'data': contact_data })

