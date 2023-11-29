from django.shortcuts import redirect, render
from django.urls import reverse
from item.models import Category, Item
from .forms import SignUpForm
from django.contrib.auth.models import User

def index(request):

    categories = Category.objects.all()
    items = Item.objects.all()

    context = {
        'categories': categories,
        'items': items,
    }

    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()


            return redirect(reverse('login/'))
        else:
            print(form.errors)
        
    else:
        form = SignUpForm()

    context = {
        'form': SignUpForm,
    }

    return render(request, 'signup.html', context)