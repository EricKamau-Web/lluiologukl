from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def agentsingle(request):
    return render(request,'agent-single.html')


def agentsgrid(request):
    return render(request,'agents-grid.html')

def bloggrid(request):
    return render(request,'blog-grid.html')

def blogsingle(request):
    return render(request,'blog-single.html')

def contact(request):
    return render(request,'contact.html')

def propertygrid(request):
    return render(request,'property-grid.html')

def propertysingle(request):
    return render(request,'property-single.html')