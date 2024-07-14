from django.shortcuts import render, redirect
from .models import Stock
from .form import StockCreateForm,StockSearchForm

# Create your views here.

def home(request):
    title = 'Home'
    context = {
        "title" : title,
    }

    return render(request, 'home.html', context)


def list_items(request):
    title = "List of Items"
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "title" : title,
        "queryset": queryset,
        "form":form
    }

    queryset = Stock.objects.all()

    if request.method == "POST":
        queryset = queryset.filter(category__icontains=form['category'].value(),
                                        item_name__icontains=form["item_name"].value())
        
        context = {
            "form":form,
            "title":title,
            "queryset":queryset,
        }


    return render(request, "list_items.html",context)



def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_items')
    context = {
        "form" : form,
        "title" : "Add Item",
    }

    return render(request,"add_items.html",context)







