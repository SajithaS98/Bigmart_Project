from django.shortcuts import render,redirect
from Backend.models import ProductDb,BigmartDb
from WebApp.models import ContactDb,RegistrationDb,CartDb
from django.contrib import messages
# Create your views here.

def homepage(request):
    cat = BigmartDb.objects.all()
    return render(request,"Home.html",{'cat':cat})

def aboutpage(req):
    cat = BigmartDb.objects.all()
    return render(req,"About.html",{'cat':cat})
def contactpage(req):
    cat = BigmartDb.objects.all()
    return render(req,"Contact.html",{'cat':cat})

def ourproducts(req):
    return render(req,"Our_products.html")
def ourproducts(req):
    cat = BigmartDb.objects.all()
    pdata = ProductDb.objects.all()
    return render(req,"Our_products.html",{'pdata':pdata,'cat':cat})

def save_contact(request):
    if request.method=="POST":
        nm = request.POST.get('name')
        em = request.POST.get('email')
        ph = request.POST.get('phone')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        obj = ContactDb(Name=nm,Email=em,Phone=ph,Subject=sub,Message=msg)
        obj.save()
        return redirect(contactpage)

def filtered_products(req,cat_name):
    data = ProductDb.objects.filter(Category=cat_name)
    return render(req,"Products_filtered.html",{'data':data})

def single_productpage(req,pro_id):
    data = ProductDb.objects.get(id=pro_id)
    return render(req,"Single_product.html",{'data':data})
def registration_page(req):
    return render(req,"Register.html")

def save_registration(request):
    if request.method=="POST":
        un = request.POST.get('name')
        em = request.POST.get('email')
        pwd = request.POST.get('password')
        obj=RegistrationDb(Username=un,Email=em,Password=pwd)
        if RegistrationDb.objects.filter(Username=un).exists():
            messages.warning(request,"Username already exists..!")
        elif RegistrationDb.objects.filter(Email=em).exists():
            messages.warning(request,"Email ID already exists..!")
        else:
            obj.save()
            messages.success(request,"Registered Successfully..!")
        return redirect(registration_page)

def UserLogin(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        pswd = request.POST.get('password')
        if RegistrationDb.objects.filter(Username=un,Password=pswd).exists():
            request.session['Username'] = un
            request.session['Password'] = pswd
            messages.success(request,"Login Successfully..!")
            return redirect(homepage)
        else:
            return redirect(registration_page)
    else:
        return redirect(registration_page)

def UserLogout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "Logout Successfully..!")
    return redirect(homepage)

def save_cart(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pn = request.POST.get('pname')
        qty = request.POST.get('quantity')
        tp = request.POST.get('tprice')
        obj=CartDb(Username=un,Product_name=pn,Quantity=qty,Total_Price=tp)
        obj.save()
        messages.success(request, "Added to Cart..!")
        return redirect(homepage)

def cart_page(request):
    data = CartDb.objects.filter(Username=request.session['Username'])
    total=0
    for d in data:
        total=total+d.Total_Price
    return render(request,"Cart.html",{'data':data,'total':total})

def delete_item(request,p_id):
    x = CartDb.objects.filter(id=p_id)
    x.delete()
    messages.error(request, "Item Removed..!")
    return redirect(cart_page)

def user_login_page(req):
    return render(req,"UserLogin.html")
