from django.shortcuts import render, redirect, get_object_or_404
from .models import InventoryItem, Supplier
from .form import InventoryItemForm


# Create your views here.

def inventory_list(request):
    items = InventoryItem.objects.select_related('supplier').all()
    low_stock = [item for item in items if item.is_low_stock()]
    return render(request, 'inventory/inventory_list.html',{
        'items': items,
        'low_stock': low_stock,
    })
def add_item(request):
    if request.method =='POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
        else:
            form = InventoryItemForm()
    else:
        form = InventoryItemForm()
    return render(request, 'inventory/add_item.html', {'form': form})

def item_detail(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    return render(request, 'inventory/item_detail.html', {'item': item})

def update_quantity(request,pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        quantity = request.POST.get('quantity' , 0)
        item.quantity = quantity
        item.save()
        return redirect('inventory_list')
    return render(request, 'inventory/update_quantity.html', {'item': item})