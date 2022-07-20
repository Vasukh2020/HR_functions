from turtle import title
from wsgiref.util import request_uri
from django.http import HttpResponse
from django.shortcuts import redirect, render

from AceLogin.models import RegisterUser
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
##theswe imports are for uploading part
from django.core.files.storage import FileSystemStorage
from AceLogin.models import Book
from .forms import BookForm
from .models import Book
##uplading imports end here 
'''''    
 def login(request):
    if request.method== "POST" :
        print("request.Post=",request.POST)
        password=request.POST.get("password")
        email=request.POST.get("email")
        RegisterUser=authenticate(email='email',password='password')
        if RegisterUser is not None:

          # A backend authenticated the credentials
        else:
    # No backend authenticated the credentials

return render (request, "AceLogin.html") 
'''
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout 

from django.contrib.auth import authenticate
def login(request):
    print("starting of login")
    if request.method== "POST" :
        print("request.Post=",request.POST)
        print('dest12')
        email=request.POST['email']
        password=request.POST['password']
        print('email')
        print('password')
        
        print('done1')
        if RegisterUser.objects.filter(email=email,password=password).exists():
            print('done2')
            user= authenticate(email=email,password=password)

            auth_login(request,user)
            event= RegisterUser.objects.get(email=email,password=password)
            firstName=event.firstName
            pk=event.pk
            # return(dynamic_AceInformation(request,pk))
            print("thee id of the uswer is ",id)
            messages.info(request,firstName)
            context={
                'firstName':event.firstName,
                'lastName':event.lastName,
                'title':event.title


            }
            print("last name",event.lastName)
            print(context)
           # return(dynamic_AceInformation(event))
           # return render(request, 'AceInformation.html',context)
            return redirect ("information")    
        else:
            
            messages.info(request,'Check email and password again')
            #message='invalid'
            print("it was here ----------------------")
            return redirect('login')
    else:
       print("it wa---------------------")
       return render(request, 'AceLogin.html')
def dynamic_AceInformation(event):
    print("last name",event.lastName)
    print("last name",event.firstName)

    """  print(obj.lastName)
    context={
        'object_list':obj
    }
    print(context['object_list'])
    print("context in dynamicace iNfo",context) """
    return redirect(information)

def Logout(request):
    messages.info(request,'Logged out sucessfully!!')
    print("loggging offfffffff")

    auth.logout(request)

    print("logggging offffffffffffffffffffffffffff")
    messages.info(request,'Logged out sucessfully!!')
    return redirect('login')


def information(request):
    my_user = request.user
    
    """firstNamme=user.firstName"""
    messages.info(request,"logged in by:")
    messages.info(request,my_user)
    print("mmy user--------------------------------------")
    print(my_user) 

    return render(request, 'AceInformation.html')

def register(request):
    def PasswordWeak(password):
        l=0
        u, p, d = 0, 0, 0
        s = password
        if (len(s) >= 8):
            for i in s:
                if (i.islower()):
                    l+=1		 
                if (i.isupper()):
                    u+=1
                if (i.isdigit()):
                    d+=1
                if(i=='@'or i=='$' or i=='_'):
                    p+=1		
        if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
            print("Valid Password")
            return(0)
        else:
            print("Invalid Password")
            return(1)

        

    print("it was hereff") 
    
    if request.method== "POST" :
        print("request.Post=",request.POST)
        firstName=request.POST.get("firstName")
        lastName=request.POST.get("lastName")
        password=request.POST.get("password")
        email=request.POST.get("email")
        title=request.POST.get("sal")
        phoneNumber= request.POST.get("phoneNumber")
        print("title",title)
        print('tetst414')
        if (len(firstName)<2):
            messages.error(request,"Enter valid name")
            return render (request, "AceRegister.html")

        if RegisterUser.objects.filter(email=email).exists():
            messages.info(request,'Email already registered')
            return render (request, "AceRegister.html")
        if RegisterUser.objects.filter(phoneNumber=phoneNumber).exists():
            messages.info(request,'Phonenumber already registered')
            return render (request, "AceRegister.html") 
        if RegisterUser.objects.filter(email=email).exists():
            messages.info(request,'Email already registered')
            return render (request, "AceRegister.html") 
        if PasswordWeak(password)==1:
             messages.info(request,'Weak password...')
             return render (request, "AceRegister.html") 




          
        else:    
            user=RegisterUser.objects.create(firstName = firstName, lastName = lastName, password= password, email= email,title=title,phoneNumber=phoneNumber)
            print("saving user")
            user.save()       
            #  print('test12')
            #  #  RegisterUser.objects.create(name = name, password= password1)
            #  #    messages.info(request,'created')
        return redirect('login')

    else:
         message="invalid"
            # messages.info(request,'invalid') 
        
         return render (request, "AceRegister.html")  



 #######
 # for the file upload part ]
 #the upload fx works for a ll kina files
def upload(request):
    context={}
    if request.method=="POST":
        uploaded_file= request.FILES['file']
        fs= FileSystemStorage()
        name=fs.save(uploaded_file, uploaded_file)
        url=fs.url(name)
        
        context['url']=fs.url(name)
        print(uploaded_file.name)
        print(uploaded_file.size)


    return render(request,'upload.html',context) 

#for pdfs etc
def listResume(request):
    books=Book.objects.all()
    return render(request, 'listResume.html',{'books':books})
def uploadResume(request):
    if request.method=="POST":
     print("the request shoewn is:",request)  
     print("the request.files shoewn is:",request.FILES)
     import os  

     form= BookForm(request.POST, request.FILES)  
     print("this iis form",form)
     ''''

                                def clean_file(self):
                                    data = self.cleaned_data['file']

                                    # check if the content type is what we expect
                                    content_type = data.content_type
                                    if content_type == 'application/pdf':
                                        return data
        else:
            raise ValidationError(_('Invalid content type'))  
     file = form.FileField()
     clean_file(file)  
     '''        
     if form.is_valid():
        form.save()
        print("form saved",form)
        Name=request.POST.get("resume")
        print("thre reusme name:",Name)
        return redirect('listResume')
    else:
        form=BookForm()
    return render(request,'uploadResume.html',{'form':form})    
