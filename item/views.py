from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .forms import NewItemForm, EditItemForm
from .models import Item
from django.contrib.auth.decorators import login_required


def items(request):
    items = Item.objects.filter(is_sold=False)

    context = {
        'items': items,
    }

    return render(request, 'items.html', context)



def item_detail(request, item_id):
    
    item = get_object_or_404(Item, id=item_id)
    related_items = Item.objects.filter(category=item.category).exclude(pk=item_id)

    context = {
        'item': item,
        'related_items': related_items,
    }

    return render(request, 'item_detail.html', context)


@login_required
def new(request):

    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
        else:
            print(form.errors)

        return redirect('item:detail', item_id=item.id)

    else:
        form = NewItemForm()

    context = {
        'form': form,
        'title': 'New Item',
    }

    return render(request, 'item_form.html', context)

@login_required
def delete(request, item_id):

    item = get_object_or_404(Item, pk=item_id)
    item.delete()

    return redirect('dashboard:index')


@login_required
def edit(request, item_id):

    item = get_object_or_404(Item, pk=item_id)


    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', item_id=item.id)
        

    else:
        form = EditItemForm(instance=item)

    context = {
        'form': form,
        'title': 'Edit Item',
    }

    return render(request, 'item_form.html', context)