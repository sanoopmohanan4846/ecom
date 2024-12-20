from django.shortcuts import render, get_object_or_404
from .cart import Cart
from ecomapp.models import Product
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.


def cart_summary(request):
    # get the cart
    cart = Cart(request)
    cart_product = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, "./cart_summary.html", {'cart_product':cart_product, "quantities":quantities, "totals":totals})



def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test fro POST
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        # lookup product in DataBase
        product = get_object_or_404(Product, id=product_id)
        
        # save to session
        cart.add(product=product, quantity=product_qty)
        
        
        # Get Cart Quantity
        cart_quantity = cart.__len__()
        
        # Return resonse
		# response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("Product Added To Cart..."))
        return response
    
        


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        
        cart.delete(product=product_id)
        
        response = JsonResponse({'product':product_id})
        messages.success(request, ("Item Deleted From Shopping Cart..."))
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
		# Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        cart.update(product=product_id, quantity=product_qty)
        
        response = JsonResponse({'qty':product_qty})
		#return redirect('cart_summary')
        messages.success(request, ("Your Cart Has Been Updated..."))
        return response
	




