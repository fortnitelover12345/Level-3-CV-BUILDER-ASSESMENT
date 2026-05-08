from django.http import HttpResponse 
from django.shortcuts import render 
def index(request):
 #   return HttpResponse("Welcome to the mainpage!")
    return render(request, 'index.html')
# Mock data for templates (replace with your database models)
TEMPLATES = [
    {"name": "Professional Template", "category": "professional", "color": "blue", "layout": "single-column", "image_url": "/static/images/template1.png"},
    {"name": "Creative Template", "category": "creative", "color": "green", "layout": "two-column", "image_url": "/static/images/template2.png"},
    {"name": "Modern Template", "category": "modern", "color": "red", "layout": "three-column", "image_url": "/static/images/template3.png"},
    {"name": "Simple Template", "category": "professional", "color": "green", "layout": "two-column", "image_url": "/static/images/template4.png"},
]

def templates_view(request):
    # Get filter values from the request
    category = request.GET.get('category')
    color = request.GET.get('color')
    layout = request.GET.get('layout')

    # Filter templates based on the selected values
    filtered_templates = TEMPLATES
    if category:
        filtered_templates = [t for t in filtered_templates if t['category'] == category]
    if color:
        filtered_templates = [t for t in filtered_templates if t['color'] == color]
    if layout:
        filtered_templates = [t for t in filtered_templates if t['layout'] == layout]

    return render(request, 'templates.html', {'templates': filtered_templates})
