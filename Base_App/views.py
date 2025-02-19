from django.shortcuts import render,HttpResponse

# Create your views here.
def Home_view(request):
    return render(request, "home.html")