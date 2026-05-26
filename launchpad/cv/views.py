from django.shortcuts import render

# Create your views here.
def templates(request):
    #return HttpResponse("This is the template page.")
    return render(request, 'cv/templates.html')

def overview(request): 
    return render(request, 'cv/overview.html')
