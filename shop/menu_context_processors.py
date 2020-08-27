from .models import Category, Product, Subscription
from .forms import SubscriptionForm
from django.http import HttpResponseRedirect
from .telegramm import send_message
from django.shortcuts import render


def category(request):
    return {"categories": Category.objects.all()}


def products(request):
    return {"products": Product.objects.all(),}


def subscription(request):
    if request.POST:
        subscriber_form = SubscriptionForm(request.POST)
        if subscriber_form.is_valid():
            subscriber_form.save()
            phone = subscriber_form.cleaned_data['phone']
            message = "*ПОДПИСКА*:" + "\n" + "*ТЕЛЕФОН*: " + str(phone)
            send_message(message)
            # return HttpResponseRedirect(request.path)
            subscriber_form = SubscriptionForm()
    else:
        subscriber_form = SubscriptionForm()
    return {'subscriber_form': subscriber_form,}

