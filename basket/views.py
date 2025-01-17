from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404('basket.Product', id=product_id)
    cart, created = 'basket.Cart'.objects.get_or_create(user=request.user)

    cart_item, created = 'basket.CartItem'.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.quantity = 1
        cart_item.save()

    return redirect('cart_view')


@login_required
def cart_view(request):
    cart, created = 'basket.Cart'.objects.get_or_create(user=request.user)
    return render(request, 'basket/cart_view.html', {'cart': cart})


@login_required
def update_cart(request, item_id, quantity):
    cart_item = get_object_or_404('basket.CartItem', id=item_id)
    cart_item.quantity = quantity
    cart_item.save()
    return redirect('cart_view')


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404('basket.CartItem', id=item_id)
    cart_item.delete()
    return redirect('cart_view')


@login_required
def checkout(request):
    cart, created = 'basket.Cart'.objects.get_or_create(user=request.user)
    if not cart.items.exists():
        return HttpResponse("Your cart is empty!")

    if request.method == 'POST':
        address_line_1 = request.POST.get('address_line_1')
        address_line_2 = request.POST.get('address_line_2', '')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        country = request.POST.get('country')
        phone_number = request.POST.get('phone_number')

        order = 'basket.Order'.objects.create(
            cart=cart,
            user=request.user,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            postal_code=postal_code,
            country=country,
            phone_number=phone_number
        )
        order.calculate_total_price()