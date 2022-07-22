
from genericpath import exists
from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from hello.models import Product
from hello.forms import ProductForm, RawProductForm
from django.template import loader
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def lhome_view(request, *args,**kwargs):
    return HttpResponse("<h1>Lheio</h1>")

def view(request, *args,**kwargs):
    return HttpResponse("<h1>Rheio</h1>")

def side1(request):
    return render(request,'side1.html')

def side2(request):
    return render(request,'side2.html',{})

def extend_part(request,*args,**kwargs):
    my_content= {"a":4,"my_text":"Something new","num":183,"my_list":[1,"asgard","jam"]
    }
    return render(request,'ex1.html',my_content)

def product_detail_view(request,pk):
    obj= Product.objects.get(id=1)
    context={
        'title':obj.title,
        'description':obj.description,
        'p':obj.price
    }
    print("request+++",request)
    return render(request,"detail.html",context)
 
def product_list_view(request):
    queryset =  Product.objects.all()
    p =Paginator(queryset,4)

    page_num= request.GET.get('page',1)
    try:
      page=p.page(page_num) 
    except EmptyPage:
      page=p.page(page_num) 
    context={
        "object_list": page
    }
    return render (request,"product_view.html",context)    
    
def creating(request):
    print("it was hereff")
    print("request.Post=",request.POST)
    if request.method== "POST" :
        print("request.Post=",request.POST)
        txt=request.POST.get("t")
       # prc=request.POST.get("p")
       # rat=request.POST.get("r")
        des=request.POST.get("d")
        Product.objects.create(title= txt, description= des)
      
        '''
        print("title",title)
        obj= Product.objects.create(title='title')
        context={
        't':obj.title }
        Id=obj.id
        obj= Product.objects.get(Id)
        context={
        't':obj.title }
        obj.save()
        print("after save")
        '''
    return render (request, "creating.html") 

def deleting(request,pk_):
    event= Product.objects.get(pk=20)
    event.delete()
    print("deleted ")
    return redirect("home")

#original if using django forms
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
           form.save()
           form = ProductForm()
           #form =...added to remove written value when added to db.
    context={
        'form': form
        }
    return render(request,"datad.html",context)

def update_venue(request,id_):
   
    obj= Product.objects.get(id=1)
    context={
        'title':obj.title,
        'description':obj.description,
        'p':obj.price}
    if request.method== "POST" :
        print("request.Post=",request.POST)
        txt=request.POST.get("t")
        des=request.POST.get("d")
       # prc=request.POST.get("p")
       # rat=request.POST.get("r")
        obj.title=txt
        obj.description=des
        print(obj.title)
        obj.save()
        print("request")
    return render(request,"update_venue.html",context) 



def dynamic_detail_view(request,pk):
    print("request+++",request)
    obj= Product.objects.get(id=pk)
    context={
        'title':obj.title,
        'description':obj.description,
        'p':obj.price
    }
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    return render(request,"detail.html",context)
    #return redirect("home")
def dynamic_update(request,pk):
    obj= Product.objects.get(id=pk)
    context={
        'title':obj.title,
        'description':obj.description,
        'p':obj.price}
    if request.method== "POST" :
        print("request.Post=",request.POST)
        txt=request.POST.get("t")
        des=request.POST.get("d")
        obj.title=txt
        obj.description=des
        print(obj.title)
        obj.save()
        print("request")
    return render(request,"update_venue.html",context)

def dynamic_delete(request,pk_):
    event= Product.objects.get(pk=pk_)
    event.delete()
    print("deleted")
    return redirect("list") 
#from django.db.models import Q
#searching op with searchNav




'''
def product_list_view(request):
    print("assasssjandjnsjcnsdfkjgdtnkbjdvndsjkvbsdjvsfnvsdjkvnds")
    if 'q' in request.GET:
        q=request.GET['searchIt']
        data=Product.objects.filter(title__icontains=q)
        #multiple_q=Q(Q(title__icontains=q)|Q(content__icontaints=q))  
        #data=Product.objects.filter(multiple_q)  
    else:
        data= Product.objects.all()
        context={
            'data':data}
    print("searching",q,"+",context)        
    return render(request,'product_view.html',context)
   ''' 
def product_list_view(request):
 print("it was here ee re r")

 if 'q' in request.GET:
        print("as it was")
        q=request.GET['q']
        print("searching",q,"+")        

        queryset=Product.objects.filter(title__icontains=q)
        context={
            'object_list':queryset}
        print("it was here")
 else:
    print("it should be herww dorsr tinme")
    queryset =  Product.objects.all()
    p =Paginator(queryset,4)

    page_num= request.GET.get('page',1)
    try:
      page=p.page(page_num) 
    except EmptyPage:
      page=p.page(page_num)
    context={
            'object_list':page}
 if 's' in request.GET:
        print("soring buy price")
        queryset=Product.objects.order_by('-price')
        context={
            'object_list':queryset}           
 return render(request,'product_view.html',context)

"""
def product_create_view(request):
  # print(request.POST)
   # bringing data to backend
   title = request.POST.get('title')
   print(title)
   context={}
   return render(request,"getpost.html",context)

 """
 
#this one with pure django form   
"""
def product_create_view(request):
 my_form= RawProductForm() 
 if request.method =="POST":
   my_form=RawProductForm(request.POST)
   if my_form.is_valid():
        Product.objects.create(** my_form.cleaned_data)
 context={
    "form": my_form
 }
 return render(request,"dgetpost.html",context)
 """