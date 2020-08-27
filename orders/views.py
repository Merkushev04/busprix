from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from shop.telegramm import send_message


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            # create data for message to telegramm
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']

            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            # clear the cart
            # cart.clear()
            # # launch asynchronous task
            # order_created.delay(order.id)
            # # set the order in the session
            # request.session['order_id'] = order.id
            # # redirect for payment
            # return redirect(reverse('payment:process'))

                # send to telegramm name product
                name_product = item['product']
                message = "*ЗАЯВКА НА ПОКУПКУ*:" + "\n" + "*ИМЯ*: " + str(first_name) + "\n" + "*ФАМИЛИЯ*: " + str(last_name) + "\n" + "*ТЕЛЕФОН*: " + str(phone) + "\n" + "*ТОВАР*: " + str(name_product)
                send_message(message)

        # Очищаем корзину.
        cart.clear()
        # order_created.delay(order.id)
        return render(request, 'orders/order/created.html', {'order': order})

    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})





