from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart, CartItem, Product

class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item.quantity = 1
            cart_item.save()

        return redirect('cart_view')

def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'basket/cart_view.html', {'cart': cart})


class UpdateCartView(LoginRequiredMixin, View):
    def post(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id)
        quantity = int(request.POST.get('quantity', 1))  # По умолчанию 1, если не указано
        cart_item.quantity = quantity
        cart_item.save()

        return redirect('cart_view')


class CheckoutView(LoginRequiredMixin, View):
    def post(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        if not cart.items.exists():
            return HttpResponse("Ваша корзина пуста!")

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

        return redirect('order_summary', pk=order.pk)