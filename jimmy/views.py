from django.shortcuts import redirect, render
from django.template import context

from jimmy.models import Item
# Create your views here.

def homepage(request):
    return render(request,"base.html")

def login(request):
    return render(request, "login.html")

def view_menu(request):
    items = Item.objects.all()

    menu = {}
    for i in items:
        if i.category not in menu:
            menu[i.category] = [i]
        else:
            menu[i.category].append(i)


    data = {"menu": menu}
    return render (request, "menu.html", context = data)

def about_us(request):
    return render(request,"about_us.html")

def contact(request):
    return render(request,"contact.html")

def signup(request):
    return render(request, "signup.html")

class Order:
    def __init__(self):
        self.contents =  {}
    def get_bill(self):
        total = 0
        for i, q in self.contents.items():
            i_cost = i.price*q
            total += i_cost
        return total

def order_view(request):
    if request.method == "POST":
        items = Item.objects.all()
        current_order = Order()
        name = request.POST["name"]
        for i in items:
            if request.POST[f"order_{i.id}"].isdigit():
                current_order.contents[i] = int(request.POST[f"order_{i.id}"])
        print(current_order.get_bill())

        return render(request,"order_preview.html", context={'order': current_order})

    else:
        return redirect('menu.url')
