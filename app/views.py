from django.shortcuts import render,redirect
from django.views import View
from .models import Customer, Product, Cart, Orderplaced
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import joblib



#                        ############ dashboard ###### 
# def predict_price(request):
#     if request.method == 'POST':
#         form = PricePredictionForm(request.POST)
#         if form.is_valid():
#             ram = form.cleaned_data['ram']
#             rom = form.cleaned_data['rom']

#             # Load the machine learning model
#             model = joblib.load('predict.joblib')

#             # Make predictions using your machine learning model
#             predicted_price = model.predict([[ram, rom]])

#             # Save input and prediction to the database
#             PricePredictionInput.objects.create(ram=ram, rom=rom)

#             return render(request, 'app/result.html', {'predicted_price': predicted_price})
#     else:
#         form = PricePredictionForm()

#     return render(request, 'app/predict.html', {'form': form})



def searchp(request):
    
    if request.method=='GET':
        search = request.GET.get('search')
        if search:
            # data=Product.objects.filter(brand__contains=search)
            mdata=Q(Q(brand__icontains=search) | Q(title__icontains=search) | Q(discounted_price__icontains=search) | Q(description__icontains=search) | Q(catagory__icontains=search))
            data=Product.objects.filter(mdata)
            return render(request,'app/search.html',{'search':search, 'data':data})
        else:
            return render(request,'app/search.html')
        
# def searchBar(request):
#     if request.method=='GET':
#         query=request.GET.get('query')
#         if query:
#             products=Product.objects.filter(discounted_price__contains=query)
#             return render(request,'app/searchbar.html',{'products':products})
#     return request(request,'app/searchbar.html',{'products':products})

class ProductView(View):
    def get(self,request):
        totalitem=0
        topwears= Product.objects.filter(catagory='TW')
        bottomwears= Product.objects.filter(catagory='BW')
        mobiles= Product.objects.filter(catagory='M')
        laptop= Product.objects.filter(catagory='L')
        if request.user.is_authenticated:
            messages.success(request, 'welcome dear customer')
            totalitem= len(Cart.objects.filter(user=request.user))
        return render(request, 'app/home.html',
        {'topwears':topwears,
        'laptop':laptop,
        'bottomwears':bottomwears,
        'mobiles':mobiles,
        'totalitem':totalitem})
    
class ProductDetailView(View):
    def get(self,request,pk):
        totalitem=0
        product=Product.objects.get(pk=pk)
        item_already_in_cart=False
        if request.user.is_authenticated:
            totalitem= len(Cart.objects.filter(user=request.user))
            item_already_in_cart=Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html',
        {'product':product, 'item_already_in_cart':item_already_in_cart})

@login_required(login_url="login")
def checkout(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem= len(Cart.objects.filter(user=request.user))
    user=request.user
    add=Customer.objects.filter(user=user)
    cart_items= Cart.objects.filter(user=user)
    
    amount=0.0
    shipping_amount=70.0
    totalamount=0.0
    cart_product=[p for p in Cart.objects.all() if p.user ==request.user]
    if cart_product:
        for p in cart_product:
            tempamount=(p.quantity*p.product.discounted_price)
            amount += tempamount
        totalamount=amount+shipping_amount
    #### zero product is going in checkout
    return render(request, 'app/checkout.html',{'add':add,'totalamount':totalamount,'cart_items':cart_items,'totalitem':totalitem})

# def searchBar(request):
#     if request.method=='GET':
#         query=request.GET.get('query')
#         if query:
#             products=Product.objects.filter(discounted_price__contains=query)
#             return render(request,'app/searchbar.html',{'products':products})
#     return request(request,'app/searchbar.html',{'products':products})

@login_required(login_url="login")
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product= Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

@login_required(login_url="login")
def show_cart(request):
        totalitem=0
        if request.user.is_authenticated:
            totalitem= len(Cart.objects.filter(user=request.user))
            user=request.user
            cart=Cart.objects.filter(user=user)
            amount=0.0
            shipping_amount=70.0
            total_amount=0.0
            cart_product=[p for p in Cart.objects.all() if p.user == user]
        
            if cart_product:
                messages.success(request, 'your cart items are here')
                for p in cart_product:
                    tempamount=(p.quantity*p.product.discounted_price)
                    amount += tempamount
                    totalamount= amount + shipping_amount
                return render(request,'app/addtocart.html',{'carts':cart,'totalamount':totalamount,'amount':amount,'totalitem':totalitem})
            else:
                messages.success(request, 'no cart item')
                return render(request, 'app/emptycart.html',{'totalitem':totalitem})
        
        
def plus_cart(request):
    if request.method == 'GET':
        prod_id= request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        
        prod_qty=Product.objects.get(id=prod_id)
        c.quantity+=1
        if (c.quantity<=prod_qty.quantity):
            # c.quantity+=1
            c.save()
            amount=0.0
            shipping_amount=70.0
            total_amount=0.0
            cart_product=[p for p in Cart.objects.all() if p.user ==request.user]
            
            for p in cart_product:
                tempamount=(p.quantity*p.product.discounted_price)
                amount += tempamount
            # prod_qty.quantity-=c.quantity
            # prod_qty.save()     
            data={
                'quantity':c.quantity,
                'amount':amount,
                'totalamount': amount + shipping_amount
                }
            return JsonResponse(data)
            
        else:
            pass
    else:
        pass


def minus_cart(request):
    if request.method == 'GET':
        prod_id= request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        prod_qty=Product.objects.get(id=prod_id)     
        c.quantity-=1
        if (c.quantity>=1):
            c.save()
            amount=0.0
            shipping_amount=70.0
            total_amount=0.0
            cart_product=[p for p in Cart.objects.all() if p.user ==request.user]
            
            for p in cart_product:
                tempamount=(p.quantity*p.product.discounted_price)
                amount += tempamount
            # prod_qty.quantity+=c.quantity
            # prod_qty.save()                   
            data={
                'quantity':c.quantity,
                'amount':amount,
                'totalamount': amount + shipping_amount
                }
            return JsonResponse(data)
        else:
            pass
    else:
        pass

@login_required(login_url="login")
def remove_cart(request):
    if request.method == 'GET':
        prod_id= request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user ==request.user]
        
        for p in cart_product:
            tempamount=(p.quantity*p.product.discounted_price)
            amount += tempamount

                
        data={
            'amount':amount,
            'totalamount': amount + shipping_amount
            }
        return JsonResponse(data)


def buy_now(request):
    return render(request, 'app/buynow.html')

@login_required(login_url="login")
def address(request):
    add= Customer.objects.filter(user=request.user)
    totalitem=0
    if request.user.is_authenticated:
            totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary','totalitem':totalitem})


# @login_required(login_url="login")
# def orders(request):
#     op= Orderplaced.objects.filter(user=request.user)
#     totalitem=0
#     if request.user.is_authenticated:
#         totalitem= len(Cart.objects.filter(user=request.user))
#         messages.success(request, 'your orders')
#     return render(request, 'app/orders.html',{'order_placed':op,'totalitem':totalitem})
# views.py

# Assuming you have imported necessary modules and classes at the beginning of your views.py file

@login_required(login_url="login")
def orders(request):
    if request.user.is_authenticated:
        order_placed_instances = Orderplaced.objects.filter(user=request.user)
        totalitem = len(Cart.objects.filter(user=request.user))

        for order_placed_instance in order_placed_instances:
            product = order_placed_instance.product
            ordered_quantity = order_placed_instance.quantity

            # Subtract the ordered quantity from the product quantity
            if product.quantity >= ordered_quantity:
                product.quantity -= ordered_quantity
                product.save()
            # else:
            #     # Handle the case where the ordered quantity is greater than the available quantity
            #     messages.warning(request, f"Insufficient quantity for {product.title} in order {order_placed_instance.id}.")

        # messages.success(request, 'Your orders')

        return render(request, 'app/orders.html', {'order_placed': order_placed_instances, 'totalitem': totalitem})
    else:
        # Handle the case where the user is not authenticated
        messages.error(request, 'Please log in to view your orders.')
        return redirect('login')  # Redirect to the login page



def topwear(request,data=None):
    totalitem=0
    if request.user.is_authenticated:
        totalitem= len(Cart.objects.filter(user=request.user))
    if data == None:
        topwears=Product.objects.filter(catagory='TW')
    elif data== 'below' :
        topwears=Product.objects.filter(catagory='TW').filter(discounted_price__lt=6000)
    elif data== 'above' :
        topwears=Product.objects.filter(catagory='TW').filter(discounted_price__gt=6000)
    elif data == 'yellow' or 'sara' or 'lee':
        topwears=Product.objects.filter(catagory='TW').filter(brand=data)
    return render(request, 'app/topwear.html',{'topwears':topwears,'totalitem':totalitem})

def laptop(request,data=None):
    totalitem=0
    if request.user.is_authenticated:
        totalitem= len(Cart.objects.filter(user=request.user))
    if data == None:
        laptops=Product.objects.filter(catagory='L')
    elif data== 'below' :
        laptops=Product.objects.filter(catagory='L').filter(discounted_price__lt=60000)
    elif data== 'above' :
        laptops=Product.objects.filter(catagory='L').filter(discounted_price__gt=60000)
    elif data == 'apple' or 'dell':
        laptops=Product.objects.filter(catagory='L').filter(brand=data)
    return render(request, 'app/laptop.html',{'laptops':laptops,'totalitem':totalitem})

def bottomwear(request,data=None):
    totalitem=0
    if request.user.is_authenticated:
        totalitem= len(Cart.objects.filter(user=request.user))
    if data == None:
        bottomwears=Product.objects.filter(catagory='BW')
    elif data== 'below' :
        bottomwears=Product.objects.filter(catagory='BW').filter(discounted_price__lt=1000)
    elif data== 'above' :
        bottomwears=Product.objects.filter(catagory='BW').filter(discounted_price__gt=1000)
    elif data == 'yellow' or 'lee':
        bottomwears=Product.objects.filter(catagory='BW').filter(brand=data)
    return render(request, 'app/bottomwear.html',{'bottomwears':bottomwears,'totalitem':totalitem})

def mobile(request, data=None):
    totalitem=0
    if request.user.is_authenticated:
        totalitem= len(Cart.objects.filter(user=request.user))
    if data == None:
        mobiles=Product.objects.filter(catagory='M')
    elif data== 'below' :
        mobiles=Product.objects.filter(catagory='M').filter(discounted_price__lt=120000)
    elif data== 'above' :
        mobiles=Product.objects.filter(catagory='M').filter(discounted_price__gt=120000)
    elif data == 'Redmi' or 'Samsung' or 'Apple':
        mobiles=Product.objects.filter(catagory='M').filter(brand=data)
#### if i'm using elif for below and above , then filter is not working, so i have used it after first if. surprisingly it's working then. ####

#here(if) also works,but if i'm using elif ,then not working
    # if data== 'below' :
    #     mobiles=Product.objects.filter(catagory='M').filter(discounted_price__lt=120000)
    # if data== 'above' :
    #     mobiles=Product.objects.filter(catagory='M').filter(discounted_price__gt=120000)
    return render(request, 'app/mobile.html',{'mobiles':mobiles,'totalitem':totalitem})

class CustomerRegistrationView(View):
    def get(self,request):
        form= CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',
                      {'form':form})
    
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html',
                      {'form':form}) 
        

@login_required(login_url="login")
def payment_done(request):
    user=request.user
    custid=request.GET.get('custid')
    customer=Customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    
    
    for c in cart:
        Orderplaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        
        c.delete()
    return redirect("orders")

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self,request):
        form= CustomerProfileForm()
        return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})
    
    def post(self,request):
        form= CustomerProfileForm(request.POST)
        if form.is_valid():
            usr=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg=Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request, 'congratulations profile updated successfully!!')
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
def predictions(request):
    return render(request,'app/predict.html')
    
# def predict_price(request):
#     if request.method == 'POST':
#         form = PricePredictionForm(request.POST)
#         if form.is_valid():
#             ram = form.cleaned_data['ram']
#             rom = form.cleaned_data['rom']

#             # Make predictions using your machine learning model
#             model = joblib.load('mlmodel/predict.joblib')
#             predicted_price = model.predict([[ram, rom]])

#             # Save input and prediction to the database
#             PricePredictionForm.objects.create(ram=ram, rom=rom)

#             return render(request, 'app/result.html', {'predicted_price': predicted_price})
#     else:
#         form = PricePredictionForm()

#     return render(request, 'app/predict_price.html', {'form': form})
