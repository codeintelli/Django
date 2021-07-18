from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from google_currency import convert
import json


""" 
todo: for class based view you need to put this command for login authentication required system
* @method_decorator(login_required, name='dispatch')

todo: for function based approch we need to put this command for login authentication
* @login_required

"""


class home(View):
    def get(self, request):
        totalitem = 0
        topwears = Product.objects.filter(category='TW')
        bottomwear = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        headphone = Product.objects.filter(category='HP')
        shoes = Product.objects.filter(category='S')
        watch = Product.objects.filter(category='W')
        bag = Product.objects.filter(category='BG')
        laptops = Product.objects.filter(category='L')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            print(totalitem)
        return render(request, 'home.html', {'topwears': topwears, 'bottomwear': bottomwear, 'mobiles': mobiles, 'headphone': headphone, 'shoes': shoes, 'watch': watch, 'bag': bag, 'laptops': laptops})


class product_detail(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)

        # it check that the product is in cart if it is exist then it will show button go to cart
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'productdetail.html', {'product': product, 'item_already_in_cart': item_already_in_cart})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'profile.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        # form = CustomerProfileForm(request.POST or None)
        form = CustomerProfileForm(request.POST)
        # if request.method == "POST" and form.is_valid():
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, locality=locality,
                           city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(
                request, 'Congratulation! profile update successfully')
            return redirect('/profile', {'form': form, 'active': 'btn-primary'})


def mobile(request, data=None):
    if data == None:
        mobilesdata = Product.objects.filter(category="M")
    elif data == 'IPHONE' or data == 'SAMSUNG':
        mobilesdata = Product.objects.filter(category="M").filter(brand=data)
    elif data == 'below':
        mobilesdata = Product.objects.filter(
            category="M").filter(discount_price__lt=50000)
    elif data == 'above':
        mobilesdata = Product.objects.filter(
            category="M").filter(discount_price__gt=50000)
    return render(request, 'mobile.html', {'mobilesdata': mobilesdata})


class CustomerRegistration(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Configuration! Registraion Successfully Completed')
        return render(request, 'customerregistration.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class AddressView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = Customer.objects.filter(user=request.user)
            return render(request, 'address.html', {'data': data, 'active': 'btn-primary'})
        else:
            return redirect('/accounts/login')


@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product_title = Product.objects.get(id=product_id)
    Cart(user=user, product=product_title).save()
    print(product_id)
    return redirect('/showcart')


@login_required
def showcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        print(cart)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discount_price)
                amount += tempamount
                total_amount = amount + shipping_amount
            return render(request, 'addtocart.html', {'cart': cart, 'total_amount': total_amount, 'amount': amount, 'shipping_amount': shipping_amount})
        else:
            return render(request, 'empty.html')
    else:
        return redirect('/accounts/login')


# def plusCart(request):
#     pass
@login_required
def plusCart(request):
    if request.method == 'GET':
        # 2nd field will be ajax id
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discount_price)
                amount += tempamount

            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount':  amount + shipping_amount,
            }

            return JsonResponse(data)


@login_required
def minusCart(request):
    if request.method == 'GET':
        # 2nd field will be ajax id
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discount_price)
                amount += tempamount

            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': amount + shipping_amount,
            }

            return JsonResponse(data)


@login_required
def removeCart(request):
    if request.method == 'GET':
        # 2nd field will be ajax id
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        print(cart_product)
        for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount

        data = {
            'amount': amount,
            'totalamount': amount + shipping_amount,
        }
        return JsonResponse(data)


@login_required
def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        add = Customer.objects.filter(user=user)
        print(add)
        cart_items = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        if not add:
            return redirect('/profile')
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discount_price)
                amount += tempamount
                total_amount = amount + shipping_amount
            a = convert('inr', 'usd', total_amount)
            main_amount = json.loads(a)
            print("main amount:- ", main_amount["amount"])
            final_amount = main_amount["amount"]
        return render(request, 'checkout.html', {'add': add, 'total_amount': total_amount, 'cart_items': cart_items,'final_amount':final_amount, 'amount': amount, 'shipping_amount': shipping_amount})
    else:
        return redirect('/accounts/login')


@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    print("custid", custid)
    customer = Customer.objects.get(id=custid)
    print("customer", customer)
    cart = Cart.objects.filter(user=user)
    print("cart", cart)
    for c in cart:
        OrderPlaced(user=user, customer=customer,
                    product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect('orders')


def buy_now(request):
    return render(request, 'buynow.html')


@login_required
def orders(request):
    if request.user.is_authenticated:
        user = request.user
        order_data = OrderPlaced.objects.all()
        return render(request, 'orders.html', {'order_data': order_data})
    else:
        return redirect('/accounts/login')


def PageNotFound(request):
    return render(request, '404.html')
