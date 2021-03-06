from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from myapp.models import CartItem
from store.models import Vendor, Item
from django.contrib.auth.decorators import login_required
from account.models import Account
import uuid
import json

# Create your views here.


def storePage(request, storeIdentifier, searchTerm):
    store = Vendor.objects.get(id=uuid.UUID(storeIdentifier))
    current_user = request.user

    items = Item.objects.filter(vendor=store)
    itemsToDisplay = items if searchTerm == "all" else items.filter(
        name__icontains=searchTerm)

    print(len(items))
    context = {
        'vendorID': storeIdentifier,
        'vendorName': store.name,
        'vendorAddress': store.address,
        'vendorHours': store.hours,
        'vendorPhone': store.phone,
        'vendorDescription': store.description,
        'itemsToDisplay': itemsToDisplay,
        'numOfItemsDisplay': len(itemsToDisplay),
        'items': items,
        'searchTerm': searchTerm
    }

    return render(request, 'store/storepage.html', context)


@login_required
def add_to_cart(request):
    if not request.user.is_authenticated:
        return homepage(request)
    if request.method == 'GET':
        itemid = request.GET.get('item_id')
        quantity = request.GET.get('quantity')

        # sanity check

        item = get_object_or_404(Item, id=itemid)
        cart_item_qs = CartItem.objects.filter(item=item, account=request.user)
        print(cart_item_qs.exists())
        if cart_item_qs.exists():
            cart_item = cart_item_qs[0]
            print(cart_item.quantity)
            qty = cart_item.quantity
            qty += int(quantity)
            print("new quantity: " + str(qty))
            if qty <= 0:
                print("removing " + cart_item_qs[0].item.name + " from the cart")
                cart_item.delete()
            else:
                cart_item.quantity = qty
                print(cart_item.quantity)
                cart_item.save()
                print("added " + str(quantity) + " " + cart_item_qs[0].item.name + "(s) to the cart")
        else:
            if int(quantity) > 0:
                cart_item = CartItem.objects.create(
                    item=item, account=request.user)
                cart_item.quantity = int(quantity)
                cart_item.save()
                print("added " + str(quantity) + " " +
                      cart_item.item.name + "(s) to the cart")

        response_data = "successful"

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps(),
            content_type="application/json"
        )

    return 1
