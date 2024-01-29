from django.shortcuts import render,redirect
from django.views.generic.base import View
from .models import Shop_list
from .models import CartItem
from django.urls import reverse


# Create your views here.



class PostView(View):
    def get(self,request):
        post = Shop_list.objects.all()
        return render(request,'shop/shop.html',{'post_list':post})
    


class SecondView(View):
    def get(self,request):
        postcategory = Shop_list.objects.all()
        return render(request,'shop/category.html',{'post_list':postcategory})





def view_cart(request):
    cart_items = CartItem.objects.all()
    total_quantity = sum(item.quantity for item in cart_items)
    return render(request, 'shop/shop.html', {'cart_items': cart_items, 'total_quantity': total_quantity})



class AddToCartView(View):
    def post(self, request, product_id):
        product = Shop_list.objects.get(pk=product_id)
        existing_item = CartItem.objects.filter(product=product).first()

        if existing_item:
            existing_item.quantity += 1
            existing_item.save()
        else:
            CartItem.objects.create(product=product, quantity=1)

        return redirect('http://127.0.0.1:8000/')