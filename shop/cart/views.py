from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.decorators.http import require_POST

from catalog.models import Watch
from .cart import Cart
from .forms import OrderCreateForm
from .models import Order, OrderItem


@login_required()
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Watch, id=product_id)
    cart.add(product=product,
             quantity=int(request.POST.getlist('quantity')[0]),
             # update_quantity=request.POST.getlist('update')[0]
             )
    return redirect('cart_detail')

@login_required()
@require_POST
def cart_update(request):
    cart = Cart(request)
    data = request.POST
    products = Watch.objects.filter(id__in=list(data.keys())[1:])
    for product in products:
        cart.add(product=product,
                 quantity=int(request.POST.get(str(product.id))[0]),
                 update_quantity=True)

    return redirect('cart_detail')

@login_required()
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Watch, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

@login_required()
def cart_detail(request):
    cart = Cart(request)
    form = OrderCreateForm()
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'order_form': form})

@login_required()
@require_POST
def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm(request.POST)
    if form.is_valid():
        order = form.save()
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()
        return redirect('order_detail', order.pk)


class OrderListView(generic.ListView):
    model = Order
    template_name = 'cart/order_list.html'


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'cart/order_detail.html'