from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import *
import json

# Create your views here.
def home(request):
    trending_products = Products.objects.filter(trending=True) 
    context = {
        'trending_products': trending_products,
    }
    return render(request, 'home.html', context)


def signin(request):
    template=loader.get_template('signin.html')
    return HttpResponse(template.render())

def collections(request):
    catagory=Catagory.objects.filter(status=0)
    context={"catagory":catagory}
    return render(request,"collections.html",context)
def collectionsview(request,name):
    if(Catagory.objects.filter(status=0)):
        products=Products.objects.filter(catagory__name=name)
        context = {"products":products,"catagory_name":name}
        return render(request,"products/index.html",context)
    else:
        messages.warning(request,"no catagory found")
        return redirect('collections')
    
def product_details(request,cname,pname):
    if (Catagory.objects.filter(name=cname,status=0)):
        if (Products.objects.filter(name=pname,status=0)):
          products=Products.objects.filter(name=pname,status=0).first()
          context = {"products":products}
          return render(request,"products/products_details.html",context)
        else:
          messages.error(request,"no products")
          return redirect('collections')
    else:
        messages.error(request,"no catagory")
        return redirect('collections')





def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been created. You can log in now')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    context={'form':form} 
    return render(request,'signin.html',context)  

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out success")
    return redirect('home')   
        
def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.loads(request.body)
            product_qty = data['product_qty']
            product_id = data['pid']
            
            
            product_status=Products.objects.get(id=product_id)   
            if product_status:
                if Cart.objects.filter(user=request.user.id,product_id=product_id):
                     return JsonResponse({'status':'Product already in cart'},status=200)
                else:
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product add to cart sucess'},status=200)
                    else:
                        return JsonResponse({'status':'Product stock not available'},status=200)
                        
            else:
                return JsonResponse({'status': 'Product not found'}, status=404)
        else:
            return JsonResponse({'status':'Login to add to cart'},status=200)
    else:
         return JsonResponse({'status':'Invalid Acess'},status=200)

def cart_view(request):
     if request.user.is_authenticated:
         cart_items = Cart.objects.filter(user=request.user)
         context = {"cart_items": cart_items}
         return render(request,"cart.html",context)
     else:
         return redirect('home')
     
def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect('home')
    

def order(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        pincode = request.POST.get("pincode")
        city = request.POST.get("city")
        Order.objects.create(
            Name=name,
            Email=email,
            Address=address,
            Pincode=pincode,
            City=city
        )
        mydata = Order.objects.all()
        context = {"mydata": mydata}
        return render(request, "order.html", context)
    mydata = Order.objects.all()
    context = {"mydata": mydata}
    return render(request, "order.html", context)




       


    
    


