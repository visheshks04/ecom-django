from django.db import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Item

@login_required
def index(request):
    items = Item.object.filter(created_by=request.user)

    context = {
        'items': items,
    }

    return render(request, 'dashboard.html', context)