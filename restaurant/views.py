# restaurant/views.py
# view functions to handle URL requests
from django.shortcuts import render
from django.http import HttpResponse
import random
import time

# list of daily special items
special_items = [
    "Bubble Milk Tea",
    "Bubble Volcano",
    "Creamy Lemon Tart",
    "Dong Ding Oolong Tea Latte",
    "Classic Fruit Tea",
    "Cassia Black Tea Mousse",
    "Passion Fruit Green Tea",
    "Hony Osmanthus Oolong",
]

# list of normal items
normal_items = [
    "Taro Green Milk Tea",
    "Taro Fresh Milk",
    "Green Tea with Honey",
    "Green Tea with Cream",
]

# Create your views here.
def main(request):
    '''Shows the main page to the user'''
    template_name = 'restaurant/main.html'

    return render(request, template_name)

def order(request):
    '''Creates a daily special item'''
    template_name = 'restaurant/order.html'
    context = {
        # chooses one tea menu from special items list and add to context dict
        "special_item": random.choice(special_items)
    }

    return render(request, template_name, context)

def confirmation(request):
    '''Process the order submissioin, and generate a result'''
    template_name = 'restaurant/confirmation.html'
    print(request.POST)

    # check if POST data was sent with the HTTP POST message
    if request.POST:
        # extract order fields into variables for context dict
        # customer information & instructions
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        instructions = request.POST['instructions']

        # prompt an error message if any of the necessary customer info is missing
        # will stay at the current order page
        if ((name == '') or (phone == '') or (email == '')):
            context = {
                "error": "Please enter your name, phone, and email information!",
                "special_item": request.POST.get('special_item', random.choice(special_items))
            }
            return render(request, 'restaurant/order.html', context)

        # prompt an error message if no order has been made
        # will stay at the current order page
        item_names = ['item1', 'item2', 'item3', 'item4', 'special_item']
        item_selected = False
        for item in item_names:
            if item in request.POST:
                item_selected = True

        if item_selected == False:
            context = {
                "error": "Please select at least one item and press place order!",
                "special_item": request.POST.get('special_item', random.choice(special_items))
            }
            return render(request, 'restaurant/order.html', context)

        # ordered items list
        ordered_items = []

        # total price
        total = 0.0

        # item 1 specific options
        sugar_level = ""
        add_boba = ""

        # check if normal items are selected
        # note that user can choose multiple items up to four normal items
        if 'item1' in request.POST:
            ordered_items.append("Taro Green Milk Tea")
            total += 12
            # extra options for item 1
            sugar_level = request.POST['sugar_level']
            add_boba = request.POST['add_boba']
        if 'item2' in request.POST:
            ordered_items.append("Taro Fresh Milk")
            total += 12
        if 'item3' in request.POST:
            ordered_items.append("Green Tea with Honey")
            total += 15
        if 'item4' in request.POST:
            ordered_items.append("Green Tea with Cream")
            total += 18

        # check if special item is selected
        if 'special_item' in request.POST:
            special_item = request.POST['special_item']
            ordered_items.append(special_item)
            total += 20

        # random ready time
        wait = random.randint(30, 60)
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_min = current_time.tm_min
        ready_hour = current_hour
        ready_min = current_min + wait
        if ready_min >= 60:
            ready_hour += 1
            ready_min -= 60
        if ready_hour >= 24:
            ready_hour -= 24
        if ready_min < 10:
            ready_time = str(ready_hour) + " : 0" + str(ready_min)
        else:
            ready_time = str(ready_hour) + " : " + str(ready_min)

        # context dict
        context = {
            "name": name,
            "phone": phone,
            "email": email,
            "instructions": instructions,
            "ordered_items": ordered_items,
            "sugar_level": sugar_level,
            "add_boba": add_boba,
            "total": total,
            "ready_time": ready_time
        }

        return render(request, template_name, context)
