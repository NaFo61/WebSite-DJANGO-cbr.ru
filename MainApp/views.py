from .forms import RegistrationForm, ReviewForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .models import *


@login_required(login_url='login')
def home(request):
    template_dir = 'app/menu.html'

    if 'q' in request.GET:
        q = request.GET['q']
        products = Product.objects.filter(name__icontains=q)
    else:
        products = Product.objects.all()

    context = {
        'products': products,
        "is_carousel": True,
        "val": "",
    }

    return render(request, template_dir, context=context)


def category(request, val):
    template_dir = 'app/menu.html'

    if 'q' in request.GET:
        q = request.GET['q']
        products = Product.objects.filter(name__icontains=q)
    else:
        products = Product.objects.filter(category=val)

    context = {
        "products": products,
        "val": val,
    }

    return render(request, template_dir, context=context)


@login_required(login_url='login')
def product_detail(request, pk):
    template_dir = 'app/shop-page.html'

    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            is_created = Review.objects.filter(user=user, product=product).exists()
            if is_created:
                rev = Review.objects.get(user=user, product=product)
                rev.text = form.cleaned_data.get("text")
                rev.save()
            else:
                review = form.save(commit=False)
                review.user = user
                review.product = product
                review.save()
    else:
        form = ReviewForm()

    context = {
        "product": product,
        "reviews": reviews,
        "review_form": form,
    }

    return render(request, template_dir, context)


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()

    return redirect('/')


def show_cart(request):
    template_dir = 'app/cart.html'

    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.cost
        amount = amount + value
    total_amount = amount

    return render(request, template_dir, locals())


def thx(request):
    template_dir = 'app/thx.html'

    user = request.user
    cart = Cart.objects.filter(user=user)

    for c in cart:
        c.delete()

    return render(request, template_dir, locals())


def register(request):
    template_dir = 'app/register.html'

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }

    return render(request, template_dir, context=context)


def user_login(request):
    template_dir = 'app/login.html'

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(request, template_dir, context=context)


@login_required
def profile(request):
    template_dir = 'app/menu.html'

    user = request.user

    context = {
        'user': user
    }

    return render(request, template_dir, context=context)
