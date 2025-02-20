from django.shortcuts import render,HttpResponse
from Base_App.models import ItemList,Items,AboutUs,Feedback
# Create your views here.
def Home_view(request):
    items = Items.objects.all()
    categories = ItemList.objects.all()  # Renamed variable
    review = Feedback.objects.all()
    return render(request, "home.html" , {'items': items, 'categories': categories,'review':review})


def About_view(request):
    return render(request, "about.html")


def Menu_view(request):
    items = Items.objects.all()
    categories = ItemList.objects.all()  # Renamed variable
    return render(request, "menu.html", {'items': items, 'categories': categories})


def Book_table_view(request):
    return render(request, "book_table.html")

def feedback(request):
    return render(request, "feedback.html")



