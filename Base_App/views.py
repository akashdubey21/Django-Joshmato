from django.shortcuts import render,HttpResponse

# Create your views here.
def Home_view(request):
    return render(request, "home.html")


def About_view(request):
    return render(request, "about.html")


def Menu_view(request):
    return render(request, "menu.html")


def Book_table_view(request):
    return render(request, "book_table.html")

def feedback(request):
    return HttpResponse("Hi!, This is my feedback page")



