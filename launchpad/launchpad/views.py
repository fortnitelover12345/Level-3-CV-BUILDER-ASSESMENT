from django.http import HttpResponse 

def mainpage(request):
    return HttpResponse("Welcome to the mainpage!")

def template(request):
    return HttpResponse("This is the template page.")